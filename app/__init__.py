
# app/__init__.py

from flask import Flask
from app import users_accounts
from app import shopping_list

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views
app.secret_key = "xbex13xfax9fxffxd0xzx1fxa1bx95x8ex1fx08xff)r|3xa0Dxa8"

# Load the config file
app.config.from_object('config')