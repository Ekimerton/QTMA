from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, SelectField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from webapp.models import User, Team
from webapp import db

class RegistrationForm(FlaskForm):
    firstname = StringField("First Name", validators=[DataRequired()])
    lastname = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=99)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Create Account")
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username already taken!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email address already taken!')

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    remember = BooleanField('Remember This Computer')
    submit = SubmitField("Continue")

class PasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError("That email address isn't registered!")

class AccountForm(FlaskForm):
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])

    picture = FileField('Update Profile Picture', validators=[FileAllowed(["jpg", "png"])])
    company_name = StringField("Company Name", validators=[DataRequired(),
        Length(max=50)])
    linked_in = StringField("LinkedIn", validators=[DataRequired(),
        Length(max=50)])
    other_link = StringField("Other", validators=[DataRequired()])
    team_name = SelectField('Team Name', validators=[DataRequired()],
            choices=[])

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username already taken!')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email address already taken!')

