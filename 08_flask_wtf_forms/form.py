from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    name = StringField("Full name", validators=[DataRequired(message="We need your name, it cannot be empty")])
    email = StringField("Email",validators=[DataRequired(), Email(message="That does not look like a valid email")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, message="Password must be at least 6 characters long")])
    submit = SubmitField("Register")