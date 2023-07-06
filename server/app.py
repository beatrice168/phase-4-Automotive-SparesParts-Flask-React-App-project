from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource


from models import db, Showroom, Customer, Showroom_customer

app = Flask(__name__)
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
            name = data['name'],
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


#get by name  showroom
#seen by the customer
class showByAccesories(Resource):
    def get(self,accessories):
        # show = Showroom.query.filter_by(accessories=accessories).first().to_dict()
        show = Showroom.query.filter_by(accessories=accessories).first()
        data = {
            "accessories":show.accessories
        }


        return make_response(jsonify(data),200)
    
    
api.add_resource(showByAccesories,"/showroom/<string:accessories>")    

#seen by the owner of the showroom
class ByName(Resource):
    def get(self,name):
        names = []
        for show in Showroom.query.filter_by(name=name).all():
            data = show.to_dict()
            names.append(data)
    
        return make_response(jsonify(names),200)
    
api.add_resource(ByName,"/show/<string:name>")     


#patch showroom

#delete showroom-accessories



#get customers




if __name__ == '__main__':
    app.run(port=5555)