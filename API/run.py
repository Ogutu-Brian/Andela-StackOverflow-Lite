"""Initializes and runs the StackOverflowLite Application"""
import v1
from v1 import user_routes
from flask import (Flask, jsonify)
from flask_jwt_extended import JWTManager


def create_app(condif_name="DEVELOPMENT"):
    app = Flask(__name__, instance_relative_config=True)
    v1.initialize_app(app)
    app.register_blueprint(user_routes, url_prefix="/api/v1/users")

    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def my_expired_token_allback():
        return jsonify({
            "status": "error",
            "message": "The toke has expired, login to get another token"
        }), 401

    @jwt.unauthorized_loader
    def unauthorized(e):
        return jsonify({
            "status": "error",
            "message": "bearer token not provided"
        }), 401

    @jwt.invalid_token_loader
    def invalid_token(e):
        return jsonify({
            "error": "error",
            "message": "invalid token provided"
        }), 401

    @app.errorhandler
    def page_not_found(e):
        return jsonify({
            "status": "error",
            "message": "Resource not found"
        }), 404
    return app


app = create_app()
if __name__ == "__main__":
    app.run()
