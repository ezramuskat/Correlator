from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class PatternForm(FlaskForm):
    name = StringField(
        'Pattern Name',
        [DataRequired()]
    )
    body = StringField(
        'Description',
        [
            DataRequired(),
            Length(min=4,
            message=('Your message is too short.'))
        ]
    )
    submit = SubmitField('Submit')