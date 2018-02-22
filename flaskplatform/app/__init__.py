from flask import Flask
from systeminfo import systeminfo

app = Flask(__name__)
from app import views
