from flask import Blueprint, render_template, request, url_for, flash, redirect, request, abort
# from webapp.main.forms import
# import webapp.main.utils as utils
import datetime

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def default():
    return render_template('index.html')
