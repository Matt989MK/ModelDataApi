from flask import Blueprint, request
from flask_restful import Api
from resources.recommendation import RecommendationResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


#api.add_resource(User, '/User')
#api.add_resource(Booking, '/Booking')
api.add_resource(RecommendationResource, '/Recommendation')
#api.add_resource(RecommendationResource.post(), '/RecommendationPost')

