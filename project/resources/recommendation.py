from flask import jsonify, request
from flask_restful import Resource
from Model import db, Recommendation, RecommendationSchema

recommendations_schema = RecommendationSchema(many=True)
recommendation_schema = RecommendationSchema()

class RecommendationResource(Resource):
    def get(self):
        recommendations = Recommendation.query.all()
        recommendations = recommendations_schema.dump(recommendations)
        return {"status":"success", "data":recommendations}, 200

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
        recommendation = Recommendation(
            name=json_data['name']
        )
        db.session.add(recommendation)
        db.session.commit()

        result = recommendation_schema.dump(recommendation).data

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = recommendation_schema.load(json_data)
        if errors:
         return errors, 422
        recommendation = Recommendation.query.filter_by(id=data['recommendation_id']).first()
        if not recommendation:
            return {'message': 'Recommendation does not exist'}, 400
        recommendation.name = data['name']
        db.session.commit()
        result = recommendation_schema.dump(recommendation).data
        return { "status": 'success', 'data': result }, 204

    def delete(self):
        json_data = request.get_json(force=True)

        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = recommendation_schema.load(json_data)
        if errors:
            return errors, 422
        recommendation = Recommendation.query.filter_by(id=data['recommendation_id']).delete()
        db.session.commit()

        result = recommendation_schema.dump(recommendation).data

        return {"status": 'success', 'data': result}, 204
