from . import db


class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'pattern-finder-users'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )


    def __repr__(self):
        return '<User {}>'.format(self.username)
#this is going to be updated to be a db model later
#likely going to change datapoints to reflect a graph
class Pattern():
	def __init__(self, name:str, patterns:list[str], datapoints:list[str]):
		self.name = name
		self.patterns = patterns
		self.datapoints = datapoints