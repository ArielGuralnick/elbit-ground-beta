import osimport pathlib

from flask import Flask, request, render_template, redirect, url_for, flashfrom flask.ext.login import (LoginManager, current_user, login_required,                            login_user, logout_user, UserMixin, AnonymousUser,                            confirm_login, fresh_login_required)
class User(UserMixin):    def __init__(self, name, id, active=True):        self.name = name        self.id = id        self.active = active    def is_active(self):        return self.activeclass Anonymous(AnonymousUser):    name = u"Anonymous"USERS = {    1: User(u"Notch", 1),    2: User(u"Steve", 2),    3: User(u"Creeper", 3, False),}USER_NAMES = dict((u.name, u) for u in USERS.itervalues())
app = Flask(__name__)SECRET_KEY = "dOVljBuSkQ"  # yeah, not actually a secretDEBUG = Trueapp.config.from_object(__name__)login_manager = LoginManager()login_manager.anonymous_user = Anonymouslogin_manager.login_view = "login"login_manager.login_message = u"Please log in to access this page."login_manager.refresh_view = "reauth"@login_manager.user_loaderdef load_user(id):    return USERS.get(int(id))
login_manager.setup_app(app)@app.route("/")def index():    return render_template("index.html")
rootDir=pathlib.Path().resolve()print("CD into dir:", rootDir)
os.chdir(rootDir)

# for safety - we go to terminal, import os, then - os.urandom(12).hex(), and copy the result and paste here.
app.config['SECRET_KEY'] = '\xe0\\\x17\xb3\xca_\x82\x94\xf4\xa8w/;\x17&\xbbr\xf4;\xb6\x8f@\xcd\x7f'

#we are importing views.py 
from app import routs

