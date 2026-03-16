from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "sua_chave_secreta" 


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mercado.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "page_login" 
login_manager.login_message_category = "info"  
from mercado import routes
from mercado import models