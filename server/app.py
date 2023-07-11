from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from models import db, Showroom, Customer, Showroom_customer

app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)

CORS(app)
# DATABASE_URI='sqlite:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

class Index(Resource):
    def get(self):
        response_dict = {
            "welcome": "Welcome to the home page",
        }
        response = make_response(
            jsonify(response_dict),
            200
        )
        return response
api.add_resource(Index, '/home')

#get  showroom
class Show(Resource):
    def get(self):
        shows = []
        for show in Showroom.query.all():
            data = show.to_dict()
            shows.append(data)
        response = make_response(jsonify(shows),200)
        return response
    
#post showroom-accessories
    def post(self):
        data = request.get_json()
        new_data = Showroom(
            # name = data['name'],
            location = data['location'],
            accessories = data['accessories'],
            description = data['description'],
            price = data['price'],
            image = data['image']
        )
        

        db.session.add(new_data)
        db.session.commit()

        return make_response(jsonify(new_data.to_dict()),201)

api.add_resource(Show,"/showroom")        

class showByAccesories(Resource):
    def get(self,accessories):
        names = []
        for show in Showroom.query.filter_by(accessories=accessories).all():
            data = show.to_dict()
            names.append(data)
    
        return make_response(jsonify(names),200)

    def patch(self,id):
        show = Showroom.query.filter_by(id=id).first()
        for attr in request.form:
            setattr(show,attr,request.form[attr])
        db.session.add(show)
        db.session.commit()
        response_dict = show.to_dict()
        response = make_response(
            jsonify(response_dict),200
        )  
        return response 

    def delete(self,id):
        show = Showroom.query.filter_by(id=id).first()
        db.session.delete(show)
        db.session.commit()

        response = make_response(
            jsonify({"message":"deleted successfully"}), 200
        )
        return response
    
    
api.add_resource(showByAccesories,"/showroom/<int:id>")    

#get customers
class Customers(Resource):
    def get(self):
        customer = []
        for custom in Customer.query.all():
            data = custom.to_dict()
            customer.append(data)
        response = make_response(jsonify(customer),200)
        return response
    
api.add_resource(Customers,"/customer")    

if __name__ == '__main__':
    app.run(port=5555)