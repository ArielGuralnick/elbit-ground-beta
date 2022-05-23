import os
import pathlib

from flask import Flask

app = Flask(__name__)


rootDir=pathlib.Path().resolve()
print("CD into dir:", rootDir)
os.chdir(rootDir)
current_cd_path = os.getcwd()
print("CD=", current_cd_path)

# for safety - we go to terminal, import os, then - os.urandom(12).hex(), and copy the result and paste here.
app.config['SECRET_KEY'] = '\xe0\\\x17\xb3\xca_\x82\x94\xf4\xa8w/;\x17&\xbbr\xf4;\xb6\x8f@\xcd\x7f'

#we are importing views.py 
from app import routs

