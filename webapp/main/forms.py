from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, SelectField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user

# Add validators for username and email to see if they are taken
class RegistrationForm(FlaskForm):
    firstname = StringField("First Name", validators=[DataRequired()])
    lastname = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=99)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Create Account")
    
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    remember = BooleanField('Remember This Computer')
    submit = SubmitField("Continue")

class PasswordResetForm(FlaskForm):
    email = StringField('Email', validators=DataRequired(), Email()])
# Add validators for username and email, same as registration
class AccountForm(FlaskForm):
    # Personal Info
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=15)])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])

    # Profile Picture
    picture = FileField('Update Profile Picture', validators=[FileAllowed(["jpg", "png"])])

    # Career Info
    company_name = StringField("Company Name", validators=[DataRequired(),
        Length(max=50)])
    linked_in = StringField("LinkedIn", validators=[DataRequired(),
        Length(max=50)])
    other_link = StringField("Other", validators=[DataRequired()])

    # Projects

    team_name = SelectField('Team Name', validators=[DataRequired()],
            choices=[])

