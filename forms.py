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


class signup(FlaskForm):
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
