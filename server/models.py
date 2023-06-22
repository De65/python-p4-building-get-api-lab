from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

    id = db.Column(db.Integer, primary_key=True)
    name= db.column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    baked_goods=db.relationship('BakedGood', backref='backery')

class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    prices= db.Column(db.Integer)
    Bakery_id=db.column(db.Integer, db.ForeignKey('bakery.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    