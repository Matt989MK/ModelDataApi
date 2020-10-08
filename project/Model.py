from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()


class Recommendation(db.Model):
    __tablename__ = 'recommendations'
    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    bookBase = db.Column(db.Integer)
    bookRecommended = db.Column(db.Integer)
    support = db.Column(db.Float)
    confidence = db.Column(db.Float)
    lift = db.Column(db.Float)

    def __init__(self, bookBase, bookRecommended, support, confidence, lift):
        self.bookBase = bookBase
        self.bookRecommended = bookRecommended
        self.support = support
        self.confidence = confidence
        self.lift = lift


class RecommendationSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    bookBase = fields.Integer(required=True)
    bookRecommended = fields.Integer(required=True)
    support = fields.Integer(required=True)
    confidence = fields.Integer(required=True)
    lift = fields.Integer(required=True)
    creation_date = fields.DateTime()
