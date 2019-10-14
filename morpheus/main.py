from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '8bf453d6ee5d32678889844e83bb649f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    positions = db.relationship('Position', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coin = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Position('{self.coin}', '{self.date_posted}')"


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


if __name__ == '__main__':
    app.run(debug=True)