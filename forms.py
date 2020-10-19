"""define the pets add form"""


from flask_wtf import FlaskForm
from wtforms import StringField, FloatField,TextAreaField,IntegerField,SelectField,BooleanField,RadioField
from wtforms.validators import InputRequired, Optional,URL,Length,NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets"""
    name = StringField("Pet Name",validators=[InputRequired()])
    species = RadioField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("bird", "Bird"),("pig",'Pig'),("monkey","Monkey"),("rabbit","Rabbit")],
    )
    photo_url = StringField("Photo Url",validators=[Optional(),URL()])
    age = IntegerField("Age",validators=[Optional(),NumberRange(min=0,max=30)])
    notes = TextAreaField("Notes",validators=[Optional(),Length(min=5)])



class EditPetForm(FlaskForm):
    """Form for editing the pet"""
    photo_url = StringField("Photo Url",validators=[InputRequired(),URL()])
    available = BooleanField("Available?")
    notes = TextAreaField("Notes",validators=[Optional(),Length(min=5)])

