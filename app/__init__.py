# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Import core packages
import os

# Import Flask 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Inject Flask magic
app = Flask(__name__)

# App Config - the minimal footprint
app.config['TESTING'] = True 

# Set up the App SECRET_KEY
SECRET_KEY = 'S_U_perS3crEt_KEY#9999'

# SQLAlchemy Settings
app.config['SQLALCHEMY_DATABASE_URI']        = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Construct the DB Object (SQLAlchemy interface)
db = SQLAlchemy (app)

# Import routing to render the pages
from app import views
