import os
import pathlib

from flask import Flask, request, render_template, redirect, url_for, flash
from flask_login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin, AnonymousUser,
                            confirm_login, fresh_login_required)


class User(UserMixin):
    def __init__(self, name, id, active=True):
        self.name = name
        self.id = id
        self.active = active

    def is_active(self):
        return self.active




class Anonymous(AnonymousUser):
    name = u"Anonymous"



rootDir=pathlib.Path().resolve()
print("CD into dir:", rootDir)
os.chdir(rootDir)

# for safety - we go to terminal, import os, then - os.urandom(12).hex(), and copy the result and paste here.
app.config['SECRET_KEY'] = '\xe0\\\x17\xb3\xca_\x82\x94\xf4\xa8w/;\x17&\xbbr\xf4;\xb6\x8f@\xcd\x7f'

#we are importing views.py 
from app import routs

