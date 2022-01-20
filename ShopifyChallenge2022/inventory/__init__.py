from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///inventory.db'
db = SQLAlchemy(app)
SECRET_KEY = 'ec9439cfc6c796ae2029594d'
app.config['SECRET_KEY'] = SECRET_KEY
from inventory import routes





