from flask import (Blueprint, jsonify, request)
from v1.routes import db
from v1.models import Question
question_routes = Blueprint("routes.question", __name__)


@question_routes.route('/questions', methods=["POST"])
def post_question():
    if request.is_json:
        valid, errors = db.questions.is_valid(request.json)
        if not valid:
            return jsonify({
                "data": errors,
                "status": "error"
            }), 400
        #create question
        result = request.json
        question = Question(
            user=result["user"], subject=result["subject"], question=result["question"])
        db.questions.insert(question)
        user = db.users.query_by_field(
            "email", question.to_json_object()["user"])
        if not user:
            return jsonify({
                "message":"User with that emmail address does not exist",
                "status":"error"
            }),400
        return jsonify({
            "data": {
                "id": db.questions.index,
                "user": user.first_name,
                "subject": question.question,
                "question": question.question,
                "created_at": question.created_at,
                "updated_at": question.updated_at
            }
        }), 201
    else:
        return jsonify({
            "message": "Request should be in JSON",
            "status": "error"
        }), 400
