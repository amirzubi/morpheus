from morpheus import db, login_manager
from datetime import datetime
from flask_login import UserMixin


##### User aus der Datenbank laden
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


##### Konto
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    positions = db.relationship('Position', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


##### Portfolioeintrag
class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coin = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Position('{self.coin}', '{self.date_posted}')"