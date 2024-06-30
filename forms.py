"""Forms for our Adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(["cat","dog","porcupine"],
                                                                        message="Must be cat, dog, or porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Must be a valid URL")])
    age = FloatField("Age", validators=[Optional(), NumberRange(min=0,max=30, message="Age must be between 0 and 30")])
    notes = StringField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Must be a valid URL")])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available")
