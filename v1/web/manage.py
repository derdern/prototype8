from flask_migrate import Migrate
from flask import Flask
from flask_script import Manager
from web.main import app
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import MigrateCommand
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
migrate = Migrate(app, db)

