from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify
from morpheus import app, db, bcrypt
from morpheus.forms import RegistrationForm, LoginForm, UpdateAccountForm, PositionForm
from morpheus.models import User, Position
from morpheus.api import *
from flask_login import login_user, current_user, logout_user, login_required
import os
import requests
import json
import secrets
import plotly
import plotly.graph_objects as go
from matplotlib import pyplot as plt
import numpy as np


##### Index
@app.route("/")
@app.route("/index")
def index():
	# Falls der User angemeldet ist, wird er zu "Portfolio" weitergeleitet
	if current_user.is_authenticated:
		return redirect(url_for("portfolio"))
	return render_template("index.html")


##### Portfolio
@app.route("/portfolio", methods=["GET", "POST"])
# Falls der User nicht angemeldet ist, wird er zu "Anmelden" weitergeleitet
@login_required
def portfolio():
	# Erfasste Positionen des akutellen Benutzers \ Nach dem der Anzahl der Kryptowährung sortieren \ Alle anzeigen
	positions = Position.query.filter_by(author=current_user)\
		.order_by(Position.amount.desc()) \
		.all()

	# Daten der API der Positionen zuordnen
	blocks = []
	for position in positions:
		for x in api:
			if (position.name).lower() == x["id"]:
				block = {
					"id_" : x["id"],
					"amount" : position.amount,
					"exchange" : position.exchange,
					"name" : x["name"],
					"symbol" : x["symbol"],
					"price" : float(x["price_usd"]),
					"percent_change_1h" : x["percent_change_1h"],
					"percent_change_24h" : x["percent_change_24h"],
					"percent_change_7d" : x["percent_change_7d"],
					"value_raw" : (float(position.amount * float(x["price_usd"]))),
					"value" : ("${0:.2f}".format(float(position.amount * float(x["price_usd"])))),
					"price" : ("${0:.7f}".format(float(x["price_usd"]))),
					"position_date_posted" : position.date_posted.strftime("%d-%m-%Y"),
					"position_id" : position.id
				}
				blocks.append(block)

	# Anzahl Positionen insgesamt
	positions_total = len(positions)
	# Falls nur eine Position erfasst wurde
	if positions_total == 1:
		positions_total_one_or_more = "Position"
	# Falls mehr als eine Position erfasst wurde
	else:
		positions_total_one_or_more = "Positionen"

	# Portfolio-Gesamtwert (Alle "value_raw" bzw. "value"-Werte ohne Formatierung zusammenrechnen)
	blocks_value_total = ("${0:.2f}".format(sum([(key["value_raw"]) for key in blocks])))

	### Plotly Pie Chart
	# Daten definieren
	labels = [(key["name"]) for key in blocks]
	values = [("{0:.2f}".format(key["value_raw"])) for key in blocks]
	# Chart definieren
	fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
	# Layout Einstellungen
	fig.update_layout(
		height=300,
	    font=dict(
	        family="Open Sans",
	        size=18,
	        color="#ffffff"),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
		margin=dict(
			l=0, r=0, t=0, b=0)
		)

	# Chart als DIV verwenden
	fig_div = plotly.offline.plot(fig, output_type="div")

	return render_template("portfolio.html", title="Portfolio", 
		blocks=blocks,
		positions_total=positions_total,
		positions_total_one_or_more=positions_total_one_or_more,
		blocks_value_total=blocks_value_total,
		fig_div=fig_div)


##### Position
@app.route("/position/<int:position_id>")
# Falls der User nicht angemeldet ist, wird er zu "Anmelden" weitergeleitet
@login_required
def position(position_id):
	position = Position.query.get_or_404(position_id)
	if position.author != current_user:
		abort(403)

	return render_template("position.html", title=position.name, position=position)


##### Position hinzufügen
@app.route("/position/new", methods=["GET", "POST"])
# Falls der User nicht angemeldet ist, wird er zu "Anmelden" weitergeleitet
@login_required
def new_position():
	form = PositionForm()
	if form.validate_on_submit():
		position = Position(name=form.name.data, amount=form.amount.data, exchange=form.exchange.data, author=current_user)
		db.session.add(position)
		db.session.commit()
		# Meldung bei erfolgreichem Erstellen
		flash('Die neue Position wurde erfolgreich hinzugefügt.', 'success')
		return redirect(url_for('index'))
	return render_template('new_position.html', title='Position hinzufügen', form=form, legend="Position hinzufügen")

##### Position bearbeiten
@app.route("/position/<int:position_id>/edit", methods=["GET", "POST"])
# Falls der User nicht angemeldet ist, wird er zu "Anmelden" weitergeleitet
@login_required
def edit_position(position_id):
	position = Position.query.get_or_404(position_id)
	if position.author != current_user:
		abort(403)
	form = PositionForm()
	# Falls die Änderungen den Richtlinien entsprechen und das Formular erfolgreich abgesendet wurde
	if form.validate_on_submit():
		# Ändern der Position in der Datenbank
		position.name = form.name.data
		position.amount = form.amount.data
		db.session.commit()
		# Meldung bei erfolgreichem Ändern
		flash("Die Position wurde erfolgreich aktualisiert.", "success")
		return redirect(url_for("position", position_id=position.id))
	elif request.method == "GET":
		form.name.data = position.name
		form.amount.data = position.amount
	return render_template("new_position.html", title='Position bearbeiten', form=form, legend="Position bearbeiten")


##### Position löschen
@app.route("/position/<int:position_id>/delete", methods=["POST"])
# Falls der User nicht angemeldet ist, wird er zu "Anmelden" weitergeleitet
@login_required
def delete_position(position_id):
	position = Position.query.get_or_404(position_id)
	if position.author != current_user:
		abort(403)
	# Löschen der Position in der Datenbank
	db.session.delete(position)
	db.session.commit()
	# Meldung bei erfolgreichem Löschen
	flash("Die Position wurde erfolgreich gelöscht.", "success")
	return redirect(url_for("index"))


##### Registrieren
@app.route("/register", methods=["GET", "POST"])
def register():
	# Falls der User bereits angemeldet ist, wird er auf Home weitergeleitet
	if current_user.is_authenticated:
		return redirect(url_for("index"))
	form = RegistrationForm()
	if form.validate_on_submit():
		# Den User zur Datenbank hinzufügen
    	# Das Passwort verschlüsseln mit bcrypt
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		# Meldung bei erfolgreichem Registrieren
		flash("Dein Account wurde erfolgreich erstellt. Du kannst Dich nun einloggen.", "success")
		return redirect(url_for("login"))
	return render_template("register.html", title="Registrieren", form=form)


##### Anmelden
@app.route("/login", methods=["GET", "POST"])
def login():
	# Falls der User bereits eingeloggt ist, wird er auf Home weitergeleitet
	if current_user.is_authenticated:
		return redirect(url_for("index"))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		# Überprüfung des Nutzernamens und des Passwortes
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			# Anmelden, wenn die Daten korrekt sind
			login_user(user, remember=form.remember.data)
			next_page = request.args.get("next")
			return redirect(next_page) if next_page else redirect(url_for("portfolio"))
		# Meldung bei gescheitertem Anmelden
		else:
			flash("Ups! Etwas ist schiefgelaufen. Bitte überprüfe Deine E-Mail oder Dein Passwort.", "danger")
	return render_template("login.html", title="Anmelden", form=form)


##### Abmelden
@app.route("/logout", methods=["GET", "POST"])
def logout():
	logout_user()
	return redirect(url_for("index"))


##### Profilbild speichern
def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	# Speicherort definieren
	picture_path = os.path.join(app.root_path, "static/img/profile_pics", picture_fn)
	
	# Grösse vor dem Upload bestimmen
	output_size = (125, 125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picture_path)

	return picture_fn


##### Konto
@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
    	# Neues Profilbild speichern
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        # Meldung beim erfolgreichen Ändern der Kontoinformationen
        flash('Deine Kontoinformationen wurden aktualisiert.', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='img/profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Mein Konto',
                           image_file=image_file, form=form)