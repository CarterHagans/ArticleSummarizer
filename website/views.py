from inspect import currentframe
import json
from operator import truediv
from pkgutil import iter_modules
from re import L
from flask import Blueprint, render_template, request,flash,redirect,session,url_for
import datetime

from sqlalchemy import false, true

# from website.models import ContactRequest, User
# from .models import User, Game
from . import db
from flask_sqlalchemy import SQLAlchemy
from email.message import EmailMessage
import ssl
import smtplib
from werkzeug.utils import secure_filename
import base64

from flask_socketio import SocketIO, send,emit
from website import socketio
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import nltk
from textblob import TextBlob
from newspaper import Article

views = Blueprint("views", __name__)


views = Blueprint('views', __name__)

@views.app_errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@views.route("home")
@views.route('/')
def home():
    return render_template("home.html")

@views.route("summary",methods=["GET","POST"])
def summary():
    if request.method == "POST":
        url = request.form.get("url")
        nltk.download('punkt')
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        session['title'] = article.title
        session['authors'] = article.authors
        session['publish_date'] = article.publish_date
        session['summary'] = article.summary
        return render_template("summary.html",title=session['title'],authors=session['authors'],publish_date=session['publish_date'],summary=session['summary'])


    else:
        return render_template("summary.html")

