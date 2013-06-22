#test for git

import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = '2008HarvardBasketball2014'

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'laurentrivard'
MAIL_PASSWORD = 'Acelx3148'

# administrator list
ADMINS = ['laurentrivard@gmail.com']


#States and provinces
STATES = [('AL', 'Alabama'), ('AB', 'Alberta'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('BC', 'British Columbia'), ('CA', 'California'), ('CO', 'Colorado'),
		  ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('ID', 'Idaho'),
		  ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'),
		  ('LA', 'Louisiana'), ('ME', 'Maine'), ('MB', 'Manitoba'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'),
		  ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Misouri'), ('MT', 'Montana'), ('NE', 'Nebraska'),
		  ('NV', 'Nevada'), ('NB', 'New Bruinswick'), ('NH', 'New Hamshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'),
		  ('NY', 'New York'), ('NF', 'Newfoundland and Labrador'), ('NC', 'North Carolina'), ('ND', 'North Dakota'),('NS', 'Nova Scotia'), ('OH', 'Ohio'), ('OK', 'Oklahoma'),
		  ('ON', 'Ontario'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('RI', 'Rhode Island'), ('SK', 'Saskatchewan'),
		  ('SC', 'South Carolina'),('SD', 'South Dakota'), ('TN', 'Tennesee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'),
		  ('VA', 'Virginia'), ('WA', 'Washington'), ('VW', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')]
COUNTRIES = [('USA', 'United States'), ('CA', 'Canada')]


#image upload
UPLOAD_FOLDER = 'app/static/pics'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif', 'jpeg'])

POST_PER_PAGE = 5