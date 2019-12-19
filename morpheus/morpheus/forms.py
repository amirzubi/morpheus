from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from morpheus.models import User
from morpheus.api import *
from morpheus.routes import *


##### Neue Position hinzufügen
class PositionForm(FlaskForm):
    # SelectField = DropdownMenu
    name = SelectField("Coin", choices=[(x["name"], x["name"]) for x in api], validators=[DataRequired()])
    exchange = SelectField("Aufbewahrungsort", choices=[(x["name"], x["name"]) for x in api_exchange] + [("Ledger Nano S", "Ledger Nano S"), ("Ledger Nano X", "Ledger Nano X"), ("Trezor One", "Trezor One"), ("Trezor Model T", "Trezor Model T")] , validators=[DataRequired()])
    # TextAreaField = Eingabefeld
    amount = TextAreaField("Menge", validators=[DataRequired()])
    # SubmitField = Bestätigungsfeld / Formular absenden
    submit = SubmitField("Hinzufügen")

##### Registrierung Formular
class RegistrationForm(FlaskForm):
    # StringField = Eingabefeld (Nur String erlaubt)
    username = StringField('Nutzername',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('E-Mail',
                        validators=[DataRequired(), Email()])
    # PasswordField = Eingabefeld für das Passwort (Wird mit Punkten ausgefüllt aus Sicherheitsgründen)
    password = PasswordField('Passwort', validators=[DataRequired()])
    confirm_password = PasswordField('Passwort bestätigen',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrieren')

    ### Validierung des Nutzernamen
    def validate_username(self, username):
        # Ist der Username bereits vergeben?
        user = User.query.filter_by(username=username.data).first()
        # Fehlermeldung, falls Username bereits existiert
        if user:
            raise ValidationError("Der Nutzername ist bereits vergeben. Bitte wähle einen anderen.")

    ### Validierung der E-Mail-Adresse
    def validate_email(self, email):
        # Ist der Username bereits vergeben?
        user = User.query.filter_by(email=email.data).first()
        # Fehlermeldung, falls E-Mail-Adresse bereits existiert
        if user:
            raise ValidationError("Dîe E-Mail-Adresse ist bereits vergeben. Bitte wähle einen andere.")
            

##### Login Formular
class LoginForm(FlaskForm):
    email = StringField('E-Mail',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    # BooleanField = Auswahlfeld (True or False)
    remember = BooleanField('Anmeldedaten merken')
    submit = SubmitField('Login')


##### Kontoinformationen Formular
class UpdateAccountForm(FlaskForm):
    username = StringField('Nutzername',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('E-Mail',
                        validators=[DataRequired(), Email()])
    # FileField = Erlaubt es dem User, eine Datei hochzuladen
    # FileAllowed = Hier werden nur die Dateiformen "JPG" und "PNG" erlaubt
    picture = FileField('Profilbild ändern', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Änderungen speichern')

    ### Validierung des Nutzernamen
    def validate_username(self, username):
        # Wenn ein neuer Username gewählt wird
        if username.data != current_user.username:
            # Ist der Username bereits vergeben?
            user = User.query.filter_by(username=username.data).first()
            # Fehlermeldung, falls Username bereits existiert
            if user:
                raise ValidationError("Der Nutzername ist bereits vergeben. Bitte wähle einen anderen.")

    ### Validierung der E-Mail-Adresse
    def validate_email(self, email):
        # Wenn eine neue E-Mail-Adresse gewählt wird
        if email.data != current_user.email:
            # Ist der Username bereits vergeben?
            user = User.query.filter_by(email=email.data).first()
            # Fehlermeldung, falls E-Mail-Adresse bereits existiert
            if user:
                raise ValidationError("Dîe E-Mail-Adresse ist bereits vergeben. Bitte wähle einen andere.")