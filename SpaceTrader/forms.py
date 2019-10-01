from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=1)])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    selectDifficulty = SelectField("Choose difficulty", choices=[("easy","Easy, you have 16 points to allocate"), ("medium","Medium, you have 12 points to allocate"), ("hard","Hard, you have 8 points to allocate")])
    allocatePilot = StringField("Pilot Skill Points", validators=[DataRequired(), Length(min=1)])
    allocateFighter = StringField("Fighter Skill Points", validators=[DataRequired(), Length(min=1)])
    allocateMerchant = StringField("Merchant Skill Points", validators=[DataRequired(), Length(min=1)])
    allocateEngineer = StringField("Engineer Skill Points", validators=[DataRequired(), Length(min=1)])
    submit = SubmitField("Log in")


