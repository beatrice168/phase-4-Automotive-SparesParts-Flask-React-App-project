from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Showroom(db.Model):
    __tablename__="showroom"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    accessories = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    image = db.Column(db.String)
    custom = db.relationship("Showroom_customer",backref="showroom")


class Customer(db.Model):
    __tablename__="customer"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    show = db.relationship("Showroom_customer",backref="customer")

class Showroom_customer(db.Model):
    __tablename__= "showroom_customer"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    showroom_id = db.Column(db.Integer, db.ForeignKey("showroom.id"))

   
    
