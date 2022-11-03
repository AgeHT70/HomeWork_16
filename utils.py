import json

from app.models import User, Order, Offer
from config import db, USER_PATH, ORDER_PATH, OFFER_PATH


def load_json(path):
    with open(path, 'r', encoding="utf-8") as file:
        return json.load(file)


def init_database():
    db.drop_all()
    db.create_all()

    # filing tables
    for user_data in load_json(USER_PATH):
        new_user = User(
            id=user_data.get('id'),
            first_name=user_data.get('first_name'),
            last_name=user_data.get('last_name'),
            age=user_data.get('age'),
            email=user_data.get('email'),
            role=user_data.get('role'),
            phone=user_data.get('phone')
        )
        db.session.add(new_user)
        db.session.commit()

    for order_data in load_json(ORDER_PATH):
        new_order = Order(
            id=order_data.get('id'),
            name=order_data.get('name'),
            description=order_data.get('description'),
            start_date=order_data.get('start_date'),
            end_date=order_data.get('end_date'),
            address=order_data.get('address'),
            price=order_data.get('price'),
            customer_id=order_data.get('customer_id'),
            executor_id=order_data.get('executor_id')
        )
        db.session.add(new_order)
        db.session.commit()

    for offer_data in load_json(OFFER_PATH):
        new_offer = Offer(
            id=offer_data.get('id'),
            order_id=offer_data.get('order_id'),
            executor_id=offer_data.get('executor_id')
        )
        db.session.add(new_offer)
        db.session.commit()
