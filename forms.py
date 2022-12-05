from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField,
    PasswordField,
    DateField,
    SelectField
)

from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    URL
)

COLOUR_CHOICES = [('1', 'red'), ('2', 'green'), ('3', 'blue'), ('4', 'yellow')]


class signUp(FlaskForm):
    username = StringField(
        "username",
        [
            DataRequired(message="Enter a valid username")
        ]
    )
    password = PasswordField(
        "password",
        [
            DataRequired("Please enter a password")
        ]
    )
    confirmPassword = PasswordField(
        'confirm password',
        [
            EqualTo(password, message='confirmed passwords must match')
        ]
    )
    submit = SubmitField('submit')


class loginToAccount(FlaskForm):
    username = StringField(
        "username",
        [
            DataRequired(message="Enter a valid username")
        ]
    )
    password = PasswordField(
        "password",
        [
            DataRequired("Please your password")
        ]
    )

    submit = SubmitField('submit')


class createShip(FlaskForm):
    shipname = StringField(
        "shipname",
        [
            DataRequired(message="Enter a valid shipname")
        ]
    )
    colour = SelectField(u'colour', choices=COLOUR_CHOICES)

    crew = StringField(
        "crew",
        [
            DataRequired(message="Select your crew")
        ]
    )

    submit = SubmitField('submit')
