from flask import render_template, url_for, flash, redirect
from morpheus import app
from morpheus.forms import RegistrationForm, LoginForm
from morpheus.models import User, Position


positions = [
    {
        'author': 'Pascal',
        'coin': 'Bitcoin',
        'amount': 1.5,
        'date_posted': '20. Oktober 2019'
    },
    {
        'author': 'Pascal',
        'coin': 'Ethereum',
        'amount': 5.5,
        'date_posted': '21. Oktober 2019'
    }
]


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', positions=positions)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Der Account mit dem Nutzernamen {form.username.data} ist erstellt worden.', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Registrieren', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'info@pazu.ch' and form.password.data == 'password':
            flash('Du bist nun eingeloggt.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Ups! Etwas ist schiefgelaufen. Bitte überprüfe Deine E-Mail oder Dein Passwort.', 'danger')
    return render_template('login.html', title='Login', form=form)