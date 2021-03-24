from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    compamy_email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    company_name = db.Column(db.String(1000))
