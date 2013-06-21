from app import db


class User(db.model):
	id = db.Column(db.Integer, primary_key= True)
	firstname = db.Column(db.String(64), index = True, unique = False)
	lastname = db.Column(db.String(64), index = True, unique = False)
	email = db.Column(db.String(120), index = True, unique = True)
	password = db.Column(db.String(128))
	address_street = db.Column(db.String(256))
	address_city = db.Column(db.String(128))
	address_state = db.Column(db.String(64))
	address_country = db.Column(db.String(128))
	address_zipcode = db.Column(db.String(20))
	total_tickets = db.Column(db.Integer)

 

class Kicks(db.model):
	id = db.Column(db.Integer, primary_key = True)
	shoe_name = db.Column(db.String(64))
	shoe_size = db.Column(db.String(5))
	shoe_condition = db.Column(db.String(64))
	date_added = db.Column(db.DateTime)
	contest_start = db.Column(db.DateTime)
	contest_end = db.Column(db.DateTime)
	winner_id = db.Column(db.Integer, db.ForeignKey('user.id'))