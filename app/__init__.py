# app/__init__.py

from flask import Flask
from app import users_accounts

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views

# Load the config file
app.config.from_object('config')