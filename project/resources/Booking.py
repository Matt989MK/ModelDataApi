from flask import jsonify, request
from flask_restful import Resource
from Model import db, Booking, BookingSchema

bookings_schema = BookingsSchema(many=True)
booking_schema = BookingSchema()

class BookingResource(Resource):
    def get(self):
        bookings = Booking.query.all()
        bookings = bookings_schema.dump(bookings).data
        return {"status":"success", "data":bookings}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = booking_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422
        booking_id = Booking.query.filter_by(id=data['booking_id']).first()
        if not booking_id:
            return {'status': 'error', 'message': 'booking not found'}, 4
