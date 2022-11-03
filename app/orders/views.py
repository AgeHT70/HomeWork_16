import json

from flask import Blueprint, request

from app.models import Order
from config import db

orders_blueprint = Blueprint('orders_blueprint', __name__)


@orders_blueprint.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        result = []
        for u in Order.query.all():
            result.append(u.to_dict())
        return json.dumps(result), 200, {'Content-Type': 'application/json'}

    if request.method == 'POST':
        order_data = json.loads(request.data)
        db.session.add(Order(
            id=order_data.get('id'),
            name=order_data.get('name'),
            description=order_data.get('description'),
            start_date=order_data.get('start_date'),
            end_date=order_data.get('end_date'),
            address=order_data.get('address'),
            price=order_data.get('price'),
            customer_id=order_data.get('customer_id'),
            executor_id=order_data.get('executor_id')
        ))
        db.session.commit()

        return 'Successful adding new order', 201


@orders_blueprint.route('/orders/<int:uid>',
                        methods=['GET', 'PUT', 'DELETE'])
def order(uid: int):
    if request.method == 'GET':
        return json.dumps(Order.query.get(uid).to_dict()), 200, {
            'Content-Type': 'application/json'}

    if request.method == 'PUT':
        order_upd = Order.query.get(uid)
        order_data = json.loads(request.data)

        order_upd.name = order_data.get('name'),
        order_upd.description = order_data.get('description'),
        order_upd.start_date = order_data.get('start_date'),
        order_upd.end_date = order_data.get('end_date'),
        order_upd.address = order_data.get('address'),
        order_upd.price = order_data.get('price'),
        order_upd.customer_id = order_data.get('customer_id'),
        order_upd.executor_id = order_data.get('executor_id')

        db.session.add(order_upd)
        db.session.commit()
        return 'Successful updating order', 201

    if request.method == 'DELETE':
        order_del = Order.query.get(uid)
        db.session.delete(order_del)
        db.session.commit()
        return 'Successful deleting user', 204
