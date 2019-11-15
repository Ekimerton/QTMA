from flask import Blueprint, render_template, request, url_for, flash, redirect, request, abort, current_app
from webapp.main.forms import RegistrationForm, LoginForm, PasswordResetForm, AccountForm
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

@main.route("/profile")
@login_required
def profile():
    form = AccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            pass
        pass
    form.first_name.data = current_user.first_name
    form.last_name.data = current_user.last_name
    title = "Profile of your mom!"
    return render_template('profile.html', form=form, title=title)

'''
@main.route('/reset_request', methods=['GET', 'POST'])
def reset_request():
    form = PasswordResetForm()
'''
