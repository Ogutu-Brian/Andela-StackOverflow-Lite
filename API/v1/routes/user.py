from flask import (Blueprint, request, jsonify)
from v1.models import User
import json
from v1.routes import db

user_routes = Blueprint("routes.user", __name__)


@user_routes.route("/signup", methods=["POST"])
def register_user():
        if request.is_json:
                valid, errors = db.users.is_valid(request.json)
                if not valid:
                        return jsonify({
                            "data": errors,
                            "status": "error"
                        }), 400
                #create a user
                result = request.json
                user = User(result["first_name"], result["last_name"],
                            result["email"], result["password"])
                db.users.insert(user)
                return jsonify({
                    "data": {
                        "user": {
                            "first_name": user.first_name,
                            "last_name": user.last_name,
                            "email": user.email,
                            "password": user.password,
                            "created_at": user.created_at,
                            "updated_at": user.updated_at
                        }
                    }
                }), 201
        else:
                return jsonify({
                    "message": "Request shold be in JSON",
                    "status": "error"
                }), 400
