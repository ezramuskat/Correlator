from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, widgets, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

#based on the example given in wtform's documentation
#https://wtforms.readthedocs.io/en/3.0.x/specific_problems/
class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

#validator for multicheckboxfields, ensures that at least one checkbox is selected without requiring that all be selected
def atleast_one(form, field):
    """Validate that at least one checkbox is selected."""
    if len(field.data) < 1:
        raise ValidationError('Please select at least one pattern.')

class PatternForm(FlaskForm):
    name = StringField(
        'Pattern Name',
        [DataRequired()]
    )
    description = StringField(
        'Description',
        [
            DataRequired(),
            Length(min=4,
            message=('Your message is too short.'))
        ]
    )
    patterns = MultiCheckboxField(
        'Patterns Used',
        [atleast_one],
        choices=[
            ('Correlation', 'Correlation'),
            ('Clusters', 'Clusters')
        ]
    )
    submit = SubmitField('Submit')

class SignupForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField(
        'Name',
        validators=[DataRequired()]
    )
    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='That password is too short! Please select a stronger password.')
        ]
    )
    confirm = PasswordField(
        'Please confirm your password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    """User Log-in Form."""
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Enter a valid email.')
        ]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')