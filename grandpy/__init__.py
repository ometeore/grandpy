from flask import Flask
from .views import app
from . import models
from . import parseur

# Connect sqlalchemy to app
models.db.init_app(app)