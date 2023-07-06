from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Showroom(db.Model, SerializerMixin):
    __tablename__="showroom"
    serialize_rules = ("-showroom_customer.showroom",)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    accessories = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    image = db.Column(db.String)
    showroom_customer = db.relationship("Showroom_customer",backref="showroom")


class Customer(db.Model, SerializerMixin):
    __tablename__="customer"
    serialize_rules = ("-showroom_customer.customer",)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    showroom_customer = db.relationship("Showroom_customer",backref="customer")

class Showroom_customer(db.Model, SerializerMixin):
    __tablename__= "showroom_customer"
    serialize_rules = ("-showroom.showroom_customer","-customer.showroom_customer",)
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    showroom_id = db.Column(db.Integer, db.ForeignKey("showroom.id"))

   
    
