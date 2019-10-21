from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from morpheus.models import User


##### Neue Position hinzufügen
class PositionForm(FlaskForm):
    name = StringField("Coin", validators=[DataRequired()])
    amount = TextAreaField("Menge", validators=[DataRequired()])
    submit = SubmitField("Hinzufügen")


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


##### Kontoinformationen Formular
class UpdateAccountForm(FlaskForm):
    username = StringField('Nutzername',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('E-Mail',
                        validators=[DataRequired(), Email()])
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