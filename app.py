from app.offers.views import offers_blueprint
from app.orders.views import orders_blueprint
from app.users.views import users_blueprint
from config import app
from utils import init_database


app.register_blueprint(users_blueprint)
app.register_blueprint(orders_blueprint)
app.register_blueprint(offers_blueprint)

init_database()

if __name__ == "__main__":
    app.run(debug=True)
