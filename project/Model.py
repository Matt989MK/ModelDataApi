from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

class Recommendation(db.Model):
    __tablename__ = "bookings"
    id = db.Column(db.Integer, primary_key=True)