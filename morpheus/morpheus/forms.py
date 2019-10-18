from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from morpheus.models import User


##### Registrierung Formular
class RegistrationForm(FlaskForm):
    username = StringField('Nutzername',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('E-Mail',
                        validators=[DataRequired(), Email()])
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
    remember = BooleanField('Anmeldedaten merken')
    submit = SubmitField('Login')