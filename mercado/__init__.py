from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy ()
app = Flask(__name__)
app.config[ 'SQLALCHEMY_DATABASE_URI'] = "sqlite:///mercado.db"
app.config["SECRET_KEY"] = 'd6d4271ff499e54dd0e6b673'
db.init_app(app)
bcrypt=Bcrypt(app)

from mercado import routes
