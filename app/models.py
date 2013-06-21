from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship, backref
from datetime import datetime

ROLE_USER = 0
ROLE_ADMIN = 1



# tickets = db.Table('tickets',
# 	db.Column('kicks_id', db.Integer, db.ForeignKey('kicks.id')),
# 	db.Column('user_id', db.Integer, db.ForeignKey('user.id')))#,
# 	#db.Column('num_tickets', db.Integer)) # why cant i have a int here...? 


class User(db.Model):
	id = db.Column(db.Integer, primary_key= True)
	firstname = db.Column(db.String(64), index = True, unique = False)
	lastname = db.Column(db.String(64), index = True, unique = False)
	email = db.Column(db.String(120), index = True, unique = True)
	password = db.Column(db.String(256))
	address_street = db.Column(db.String(256))
	address_city = db.Column(db.String(128))
	address_state = db.Column(db.String(64))
	address_country = db.Column(db.String(128))
	address_zipcode = db.Column(db.String(20))
	total_tickets = db.Column(db.Integer)
	shoe_size = db.Column(db.Integer)
	role = db.Column(db.SmallInteger, default = ROLE_USER)
	joined = db.Column(db.DateTime)

	def get_id(self):
		return unicode(self.id)
	def __repr__ (self):
		return '<User %r>' % (self.firstname)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False


class Kicks(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	picture = db.Column(db.String(128))
	picture2 = db.Column(db.String(128))
	picture3 = db.Column(db.String(128))
	picture4 = db.Column(db.String(128))
	shoe_name = db.Column(db.String(64))
	shoe_size = db.Column(db.String(5))
	shoe_condition = db.Column(db.String(64))
	date_added = db.Column(db.DateTime)
	contest_start = db.Column(db.DateTime)
	contest_end = db.Column(db.DateTime)
	winner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	text = db.Column(db.String(128))

	def contestIsActive(self):
		if self.contest_start < datetime.now() and self.contest_end > datetime.now():
			return True
		else:
			return False

	def __repr__ (self):
		return '<Kicks %r>' % (self.shoe_name)

class Tickets(db.Model):
#	__tablename__ = 'tickets'
	id = db.Column(db.Integer, primary_key = True)
	num_tickets = db.Column(db.Integer)
	kicks_id = db.Column(db.Integer, db.ForeignKey('kicks.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	date = db.Column(db.DateTime)





