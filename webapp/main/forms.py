from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, SelectField, StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from webapp.models import User, Team
from webapp import db

class RegistrationForm(FlaskForm):
    firstname = StringField("First Name", validators=[InputRequired()])
    lastname = StringField("Last Name", validators=[InputRequired()])
    email = StringField("Email Address", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=99)])
    confirm_password = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo("password")])
    submit = SubmitField("Create Account")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email address already taken!')

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8)])
    remember = BooleanField('Remember This Computer')
    submit = SubmitField("Continue")

class PasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError("That email address isn't registered!")

class PersonalForm(FlaskForm):
    email = StringField("Email Address", validators=[InputRequired(), Email()])
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name = StringField("Last Name", validators=[InputRequired()])
    submit_personal = SubmitField("Save Settings")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email address already taken!')

class PictureForm(FlaskForm):
    picture = FileField('Update Profile Picture', validators=[FileAllowed(["jpg", "png"])])
    submit_picture = SubmitField("Save Settings")

class TeamForm(FlaskForm):
    team_name = SelectField('Team Name', validators=[])
    submit_team = SubmitField("Save Settings")

class CareerForm(FlaskForm):
    company_name = StringField("Company Name", validators=[InputRequired(),
        Length(max=50)])
    position = StringField("Position", validators=[InputRequired(),
        Length(max=50)])
    linked_in = StringField("LinkedIn", validators=[InputRequired(),
        Length(max=50)])
    other_link = StringField("Other", validators=[InputRequired()])
    submit_career = SubmitField("Save Settings")

