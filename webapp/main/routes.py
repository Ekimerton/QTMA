from flask import Blueprint, render_template, request, url_for, flash, redirect, request, abort, current_app
from webapp.main.forms import RegistrationForm, LoginForm, PasswordResetForm, PersonalForm, PictureForm, TeamForm, CareerForm
from flask_login import login_user, current_user, logout_user, login_required
import datetime
from webapp.models import User, Team
from webapp import db, bcrypt

main = Blueprint('main', __name__)

# Static pages
@main.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Dynamic pages
@main.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(first_name=form.firstname.data, last_name=form.lastname.data, email=form.email.data, password=hashed_pass)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("main.login"))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for("main.home"))
        flash(f"Login unsuccessful. Please check your email and password!", "danger")
    return render_template('login.html', form=form)

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))

@main.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    personal_form = PersonalForm()
    picture_form = PictureForm()
    team_form = TeamForm()
    career_form = CareerForm()

    # Add code for fetching admin-approved teams
    team_form.team_name.choices = [('1', 'Team 1'), ('2', 'Team 2'), ('3', 'Test Team')]
    if personal_form.submit_personal.data and personal_form.validate_on_submit():
        print(personal_form.email.data)
        print(personal_form.first_name.data)
        print(personal_form.last_name.data)
    if team_form.submit_team.data and team_form.validate():
        print(team_form.team_name.data)
    if career_form.submit_career.data and career_form.validate():
        print(career_form.company_name.data)

    # Name and Profile Picture
    name = current_user.first_name + " " + current_user.last_name
    propic = url_for('static' , filename="propics/" + current_user.image_file)
    # Personal Info Filling
    personal_form.email.data = current_user.email
    personal_form.first_name.data = current_user.first_name
    personal_form.last_name.data = current_user.last_name

    # Career Info Filling
    career_form.company_name.data = current_user.company
    career_form.position.data = current_user.position
    career_form.linked_in.data = current_user.linkedin
    career_form.other_link.data = current_user.other_link

    return render_template('profile.html', personal_form=personal_form, picture_form=picture_form, team_form=team_form, career_form=career_form, name=name, propic=propic)

'''
@main.route('/reset_request', methods=['GET', 'POST'])
def reset_request():
    form = PasswordResetForm()
'''
