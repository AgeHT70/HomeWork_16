import json

from flask import Blueprint, request

from app.models import Offer
from config import db

offers_blueprint = Blueprint('offers_blueprint', __name__)


@offers_blueprint.route('/offers', methods=['GET', 'POST'])
def offers():
    if request.method == 'GET':
        result = []
        for u in Offer.query.all():
            result.append(u.to_dict())
        return json.dumps(result), 200, {'Content-Type': 'application/json'}

    if request.method == 'POST':
        offer_data = json.loads(request.data)
        db.session.add(Offer(
            id=offer_data.get('id'),
            order_id=offer_data.get('order_id'),
            executor_id=offer_data.get('executor_id')
        ))
        db.session.commit()

        return 'Successful adding new offer', 201


@offers_blueprint.route('/offers/<int:uid>',
                        methods=['GET', 'PUT', 'DELETE'])
def offer(uid: int):
    if request.method == 'GET':
        return json.dumps(Offer.query.get(uid).to_dict()), 200, {
            'Content-Type': 'application/json'}

    if request.method == 'PUT':
        offer_upd = Offer.query.get(uid)
        offer_data = json.loads(request.data)

        offer_upd.order_id = offer_data.get('order_id')
        offer_upd.executor_id = offer_data.get('executor_id')

        db.session.add(offer_upd)
        db.session.commit()
        return 'Successful updating offer', 201

    if request.method == 'DELETE':
        offer_del = Offer.query.get(uid)
        db.session.delete(offer_del)
        db.session.commit()
        return 'Successful deleting offer', 204
