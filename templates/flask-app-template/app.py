# Import libraries
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Entity

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    db = setup_db(app)
    CORS(app)

    # Use the after_request decorator to set Access-Control-Allow
    # CORS Headers 
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/', methods = ['GET'])
    def welcome():
        return "Welcome to my app!"

    def get_all_entries():
        entries = [entry.format() for entry in Entity.query.order_by(Entity.date_included.desc()).all()]

        if (len(entries) == 0):
            abort(404)

        return jsonify({
        'success':True,
        'entries':oentriesffers,
        'num_entries':len(entries)
        })

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unprocessable'
        }), 422

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)