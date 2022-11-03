import json

from flask import Blueprint, request

from app.models import User
from config import db

users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        result = []
        for u in User.query.all():
            result.append(u.to_dict())
        return json.dumps(result), 200, {'Content-Type': 'application/json'}

    if request.method == 'POST':
        user_data = json.loads(request.data)
        db.session.add(User(
            id=user_data.get('id'),
            first_name=user_data.get('first_name'),
            last_name=user_data.get('last_name'),
            age=user_data.get('age'),
            email=user_data.get('email'),
            role=user_data.get('role'),
            phone=user_data.get('phone')
        ))
        db.session.commit()

        return 'Successful adding new user', 201


@users_blueprint.route('/users/<int:uid>',
                       methods=['GET', 'PUT', 'DELETE'])
def user(uid: int):
    if request.method == 'GET':
        return json.dumps(User.query.get(uid).to_dict()), 200, {
            'Content-Type': 'application/json'}

    if request.method == 'PUT':

        user_upd = User.query.get(uid)
        user_data = json.loads(request.data)

        user_upd.first_name = user_data.get("first_name")
        user_upd.last_name = user_data.get("last_name")
        user_upd.age = user_data.get("age")
        user_upd.email = user_data.get("email")
        user_upd.role = user_data.get("role")
        user_upd.phone = user_data.get("phone")

        db.session.add(user_upd)
        db.session.commit()
        return 'Successful updating user', 201

    if request.method == 'DELETE':
        user_del = User.query.get(uid)
        db.session.delete(user_del)
        db.session.commit()
        return 'Successful deleting user', 204
