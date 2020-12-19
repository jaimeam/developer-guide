import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import date

database_path = "postgresql://<user>:<password>@localhost/<db_name>"
# database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

# Bind a flask application and a SQLAlchemy service
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    migrate = Migrate(app, db)
    db.init_app(app)
    db.create_all()

    return db

# Create entity called Entity
class Entity(db.Model):
  __tablename__ = 'Entity'

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  date_included = Column(DateTime)

  def __init__(self, name, date_included):
    self.name = name
    self.date_included = date_included

  # Insert new model in database
  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  # Update model in database
  def update(self):
    db.session.commit()

  # Delete model from database
  def delete(self):
      db.session.delete(self)
      db.session.commit()

  # Form representation of Entity model
  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'date_included': self.date_included
    }