from flask import Blueprint
from flask_restful import Api
from resources.user import User
from resources.Booking import Booking
from resources.Recommendation import Recommendation



api_bp = Blueprint('api', __name__)
api = Api(api_bp)


api.add_resource(User, '/User')
api.add_resource(Booking, '/Booking')
api.add_resource(Recommendation, '/Recommendation')
