from flask.ext.wtf import Form, TextField, BooleanField, PasswordField, validators, SelectField, SubmitField, DateTimeField, TextAreaField, RecaptchaField
from flask.ext.wtf import Required, EqualTo, Email
from datetime import datetime, timedelta
from config import STATES, COUNTRIES

class LoginForm(Form):
	email = TextField ('email', validators = [Required()])
	password = PasswordField('password', validators = [Required()])
	remember_me = BooleanField('remember_me', default = False)

class AddKicksForm(Form):
	# picture = TextField('picture', validators = [Required()])
	shoe_name = TextField('shoe_name', validators = [Required()])
	shoe_size = TextField('shoe_size', validators = [Required()])
	shoe_condition = TextField('shoe_condition', validators = [Required()])
	text = TextField('text', validators = [Required()])
	# date_added = datetime.now()
	# contest_start = datetime.now()
	# contest_end = datetime.now() + timedelta(weeks=1)

class SignUpForm(Form):
	firstname = TextField('firstname', validators =[Required()])
	lastname = TextField('lastname', validators =[Required()])
	email = TextField('email', validators =[Required(), Email()])
	password = PasswordField('password', validators =[Required()])
	confirm_password =  PasswordField('confirm_password', validators =[Required(), EqualTo('password', message="Passwords must match")])
	address_street = TextField('address_street', validators =[Required()])
	address_city = TextField('address_city', validators =[Required()])
	address_state = SelectField('address_state', choices= STATES, validators =[Required()])
	address_zipcode = TextField('address_zipcode', validators =[Required()])
	address_country = SelectField('address_country', choices= COUNTRIES, validators =[Required()])

class EditAccountInfo(Form):
	firstname = TextField('firstname', validators =[Required()])
	lastname = TextField('lastname', validators =[Required()])
	email = TextField('email', validators =[Required()])
	address_street = TextField('address_street', validators =[Required()])
	address_city = TextField('address_city', validators =[Required()])
	address_state = SelectField('address_state', choices= STATES, validators =[Required()])
	address_zipcode = TextField('address_zipcode', validators =[Required()])
	address_country = SelectField('address_country', choices= COUNTRIES, validators =[Required()])


TICKET_CHOICES = [(1, "1 ticket for $2.50"), (3, "3 tickets for $5.00"), (6, "6 tickets for $10.00"), (10, "10 tickets for $15.00"),
				 (15, "15 tickets for $20.00"), (25, "25 tickets for $25.00")]

class BuyTicketsForm(Form):
	amount = SelectField('amount', choices = TICKET_CHOICES, validators = [Required()], coerce = float)


class ChangePassword(Form):
	old = PasswordField('old_pass', validators=[Required()])
	new = PasswordField('new_pass', validators=[Required()])
	confirm_new = PasswordField('confirm_new_pass', validators=[Required()])

class ContactUs(Form):
	fullname = TextField('fullname', validators=[Required()])
	email = TextField('email', validators=[Required()])
	message = TextAreaField('message', validators=[Required()])
	recaptcha = RecaptchaField()




