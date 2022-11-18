from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def init_app():
	"""Initialize the core application."""
	app = Flask(__name__, instance_relative_config=False)
	app.config.from_object('config.Config')
	db.init_app(app)
	login_manager.init_app(app)

	with app.app_context():
		# Include our Routes
		from . import routes

		return app