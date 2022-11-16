from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Length

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
        [DataRequired()],
        choices=[
            ('Correlation', 'Correlation'),
            ('Clusters', 'Clusters')
        ]
    )
    submit = SubmitField('Submit')