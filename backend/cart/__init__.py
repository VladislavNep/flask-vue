from flask import Flask
from backend import config


app = Flask(__name__)
app.config.from_object(config)


from . import views