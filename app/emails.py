from flask.ext.mail import Message
from app import mail, app
from flask import render_template
from config import ADMINS
from threading import Thread
from decorators import async

@async
def send_async_email(msg):
	with app.app_context():
		mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(msg)

def send_feedback (fullname, email, message):
	send_email(	'User Feedback',
				ADMINS[0],
				ADMINS,
				render_template("feedback_email.txt",
					fullname = fullname, 
					email = email,
					message = message),
				render_template("feedback_email.html",
					fullname = fullname, 
					email = email,
					message = message))
