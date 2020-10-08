from flask import jsonify, request
from flask_restful import Resource
from Model import db, Recommendation, RecommendationsSchema

recommendations_schema = RecommendationsSchema(many=True)
recommendation_schema = RecommendationsSchema()

class BookingResource(Resource):
    def get(self):
        recommendation = Recommendation.query.all()
        recommendation = recommendations_schema.dump(recommendation).data
        return {"status":"success", "data":recommendation}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = recommendation_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422
        recommendation_id = Recommendation.query.filter_by(id=data['recommendation_id']).first()
        if not recommendation_id:
            return {'status': 'error', 'message': 'recommendation not found'}, 4
