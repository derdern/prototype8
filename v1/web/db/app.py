
#app for  
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__) #create flask app object
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_db.db' #tell where is database
app.secret_key = "flask rocks!" #setup secret key
db = SQLAlchemy(app) #create db object for integrate SQLAlchemy into Flask