from flask import render_template, url_for, flash, redirect, request
from morpheus import app, db, bcrypt
from morpheus.forms import RegistrationForm, LoginForm
from morpheus.models import User, Position
from flask_login import login_user, current_user, logout_user, login_required


positions = [
    {
        "author": "Pascal",
        "coin": "Bitcoin",
        "amount": 1.5,
        "date_posted": "20. Oktober 2019"
    },
    {
        "author": "Pascal",
        "coin": "Ethereum",
        "amount": 5.5,
        "date_posted": "21. Oktober 2019"
    }
]


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
	return render_template("portfolio.html", title="Portfolio", positions=positions)


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


##### Account
@app.route("/account", methods=["GET", "POST"])
# Falls der User nicht angemeldet ist, wird er zu "Anmelden" weitergeleitet
@login_required
def account():
	return render_template("account.html", title="Mein Konto")