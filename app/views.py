from app import app, db, lm, mail
from forms import LoginForm, AddKicksForm, SignUpForm, BuyTicketsForm, ChangePassword, EditAccountInfo, ContactUs
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from models import User, Kicks, Tickets, ROLE_USER, ROLE_ADMIN
from werkzeug import check_password_hash, generate_password_hash, secure_filename
import random, os
from flask.ext.mail import Message
from config import ADMINS, STATES, UPLOAD_FOLDER, ALLOWED_EXTENSIONS, POST_PER_PAGE
from collections import Counter
from datetime import datetime, timedelta
from flask import Response

@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>', methods = ["GET", "POST"])
def index(page =1):
	kicks = Kicks.query.order_by(Kicks.date_added.desc()).paginate(page, POST_PER_PAGE, True)
	if g.user: #checks that the user is logged in
		tix = Tickets.query.filter_by(user_id = g.user.id).all()
	for x in range(len(kicks.items)):
		user = User.query.filter_by(id = kicks.items[x].winner_id).first()
		num_tix = 0 #initializes num tickets for each shoe
		if user: #if there is a winner
			kicks.items[x].firstname = user.firstname
			kicks.items[x].city = user.address_city
			kicks.items[x].state = user.address_state
		else: #no winner yet
			if g.user: #if user is logged in
				for t in tix:
					if t.kicks_id == kicks.items[x].id:
						num_tix += t.num_tickets
			kicks.items[x].num_tickets = num_tix
	return render_template('index.html',
		title = 'Home',
		posts = kicks)


@app.route('/test2', methods = ["POST", "GET"])
def test2():
	kicks = Kicks.query.order_by(Kicks.date_added.desc()).all()
	return Response(response= kicks,
					status = 200,
					mimetype = 'text/json')



@app.route('/login', methods = ["POST", "GET"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email = form.email.data).first()
		if user and check_password_hash(user.password, form.password.data):
			session['user_id'] = user.id
			return redirect(request.args.get("next") or url_for("index"))
		else:
			flash('Wront username/password')
	return render_template('login.html',
		title = 'Sign In',
		form = form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))
@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.before_request
def before_request():
	g.user = None
	if 'user_id' in session:
		g.user = User.query.get(session['user_id']);

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/add_kick_post', methods = ["POST", "GET"])
@login_required
def add_kick_post():
	form = AddKicksForm()
	if form.validate_on_submit():
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(UPLOAD_FOLDER, filename))
		file = request.files['file2']
		if file and allowed_file(file.filename):
			filename2 = secure_filename(file.filename)
			file.save(os.path.join(UPLOAD_FOLDER, filename2))
		file = request.files['file3']
		if file and allowed_file(file.filename):
			filename3 = secure_filename(file.filename)
			file.save(os.path.join(UPLOAD_FOLDER, filename3))
		file = request.files['file4']
		if file and allowed_file(file.filename):
			filename4 = secure_filename(file.filename)
			file.save(os.path.join(UPLOAD_FOLDER, filename4))
		new = Kicks(picture = filename,
			picture2 = filename2,
			picture3 = filename3,
			picture4 = filename4, 
			shoe_name = form.shoe_name.data, 
			shoe_size = form.shoe_size.data, 
			shoe_condition = form.shoe_condition.data, 
			winner_id = 0,
			text = form.text.data,
			date_added = datetime.now(),
			contest_start = datetime.now(),
			contest_end = datetime.now() + timedelta(weeks=1))
		db.session.add(new)
		db.session.commit()
		flash('Kicks were added')
		return redirect(url_for('index'))
	else: 
		print form.errors
	if g.user.role == ROLE_ADMIN:	
		return render_template('add_kick_post.html',
			title ='Add Post',
			form = form)
	else:
		# kicks = Kicks.query.all()
		flash('You are not allowed to visit this page')
		return redirect(url_for('index'))



@app.route('/signUp', methods = [ "POST", "GET"])
def signUp():
	form = SignUpForm()
	print 'page loaded'
	if form.validate_on_submit():
		already = User.query.filter_by(email = form.email.data).first()
		if not already:
			new_user = User(firstname = form.firstname.data, 
					lastname = form.lastname.data,
					email = form.email.data,
					password = generate_password_hash(form.password.data),
					address_street = form.address_street.data,
					address_city = form.address_city.data,
					address_state = form.address_state.data,
					address_zipcode = form.address_zipcode.data,
					address_country = form.address_country.data,
					total_tickets = 0,
					joined = datetime.now())
			db.session.add(new_user)
			db.session.commit()
			session['user_id'] = new_user.id
			print new_user.firstname
			flash('Welcome!')
			return redirect(url_for('index'))
		else:
			flash('An account with this email address already exists')
	else:
		print form.errors
		print 'hello'
	return render_template('signUp.html',
		title = "Sign Up",
		form = form)


@app.route('/buy_tickets/<shoe_id>', methods = ["GET", "POST"])
@login_required
def buyTickets(shoe_id):
	kicks = Kicks.query.filter_by(id = shoe_id).first()
	print kicks
	form = BuyTicketsForm()
	if form.validate_on_submit():
		print g.user
		if g.user:
			new_tix = Tickets(num_tickets = form.amount.data,
		 		kicks_id = kicks.id,
		 		user_id = g.user.id,
		 		date = datetime.now())
		 	db.session.add(new_tix)
		 	db.session.commit()
		return redirect(url_for('index'))
	
	ended = kicks.contestIsActive()
	print ended

	return render_template('buy_tickets.html',
		title="Buy Tickets",
		form = form,
		post = kicks,
		state = ended)


@app.route('/end_contest/<shoe_id>', methods = ["GET", "POST"])
@login_required
def endContest(shoe_id):
	all_tix = []
	tickets = Tickets.query.filter_by(kicks_id = shoe_id).all()
	if tickets:
		for t in tickets:
			for k in range(t.num_tickets):
				all_tix.append(t.user_id)

		winner_id = random.choice(all_tix)
		print winner_id
		kick = Kicks.query.filter_by(id = shoe_id).first()
		kick.winner_id = winner_id
		db.session.add(kick)
		db.session.commit()
		winner = User.query.filter_by(id = winner_id).first()
		msg = Message('test subject', sender = ADMINS[0], recipients = ADMINS)
		msg.body = 'text body'
		msg.html = '<b>HTML</b> body'
		mail.send(msg)

		flash("Contest has ended, winner is " +str(winner_id))
		return redirect(url_for('index'))
	else:
		flash('No one has bought tickets')
		return redirect(url_for('index'))

@app.route('/test')
def test():
	shoe = Kicks.query.filter_by(id = 5).first()
	return render_template('test.html',
		post = shoe)

@app.route('/about_us', methods= ["GET", "POST"])
def about():
	form = ContactUs()

	if form.validate_on_submit():
		# msg = Message('Customer feedback', sender= ADMINS[0], recipients='info@lotto-kicks.com')
		# msg.body = 'hello'#form.fullname.data# + " (" + form.email.data + ") said: \n " + form.message.data)
		# # msg.html = '<b> HTML </b> body'
		# mail.send(msg)

		msg = Message('test subject', sender = ADMINS[0], recipients = 'laurentrivard@gmail.com')
		msg.body = 'text body'
		msg.html = '<b>HTML</b> body'
		mail.send(msg)

	return render_template('about_us.html',
		form = form)

@app.route('/account/<user_id>', methods = ["GET", "POST"])
@login_required
def user(user_id):
	user = User.query.filter_by(id = user_id).first()
	kicks = Kicks.query.all()
	form = ChangePassword()
	account = EditAccountInfo(obj=user)
	tix_per_kick = []
	tix_count = []
	all_tix = Tickets.query.filter_by(user_id = user_id).all()
	for t in all_tix:
		print t.kicks_id, t.num_tickets
		kick = Kicks.query.filter_by(id = t.kicks_id).first()
		print kick.shoe_name
		obj = {'kick': kick, 'num_tickets': t.num_tickets, 'date': t.date}
		tix_count.append(obj)



 	#updates password
	if form.validate_on_submit():
		if check_password_hash(user.password, form.old.data):
			if form.new.data == form.confirm_new.data:
				user.password = generate_password_hash(form.new.data)
				db.session.add(user)
				db.session.commit()
				flash('Password was updated')
			else:
				flash('Make sure the new password matches')
		else:
			flash('Wrong password')
	#edit account info
	if account.validate_on_submit():
		print 'account was updated'
		user.firstname = account.firstname.data 
		user.lastname = account.lastname.data
		user.email = account.email.data
		user.address_street = account.address_street.data
		user.address_city = account.address_city.data
		user.address_state = account.address_state.data
		user.address_zipcode = account.address_zipcode.data
		user.address_country = 'USA'
		#Commits changes
		db.session.add(user)
		db.session.commit()
		flash('Info updated!')
	else:
		print account.errors

	print g.user.id
	print user_id
	if int(g.user.id) == int(user_id):
		return render_template('account.html',
			user = user,
			form = form,
			tix = tix_count,
			edit_form = account)
	else:
		return render_template('unauthorized.html')





