# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Import core packages
import os

# Import Flask 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inject Flask magic
app = Flask(__name__)

# Load configuration
app.config.from_object('app.config.Config')

# Construct the DB Object (SQLAlchemy interface)
db = SQLAlchemy (app)

# Import routing to render the pages
from app import views, models
