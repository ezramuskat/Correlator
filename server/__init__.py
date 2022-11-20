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
		from . import auth

		app.register_blueprint(routes.main_bp)
		app.register_blueprint(auth.auth_bp)

		db.create_all()

		return app