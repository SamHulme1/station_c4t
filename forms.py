from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField,
    PasswordField,
    DateField,
    SelectField,
    validators
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
        "username", validators=[DataRequired()])

    password = PasswordField(
        "password", validators=[DataRequired()])

    confirmPassword = PasswordField(
        'confirm password', validators=[DataRequired()]
    )

    submit = SubmitField('submit')


class loginToAccount(FlaskForm):
    username = StringField(
        "username", validators=[DataRequired()])
    password = PasswordField(
        "password", validators=[DataRequired()])
    submit = SubmitField('submit')


class createShip(FlaskForm):
    shipname = StringField(
        "shipname", validators=[DataRequired()])
    colour = SelectField(u'colour', choices=COLOUR_CHOICES)

    crew = TextAreaField(
        "crew", validators=[DataRequired()])

    submit = SubmitField('submit')


class deleteAccount(FlaskForm):
    username = StringField(
        "username", validators=[DataRequired()])
    password = PasswordField(
        "password", validators=[DataRequired()])
    confirmPassword = PasswordField(
        'confirm password', validators=[DataRequired()]
    )
    submit = SubmitField('submit')


class ChangePassword(FlaskForm):
    username = StringField(
        "username", validators=[DataRequired()])
    password = PasswordField(
        "password", validators=[DataRequired()])
    newpassword = PasswordField(
        "new password", validators=[DataRequired()])
    submit = SubmitField('submit')
