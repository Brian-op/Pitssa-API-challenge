from flask import Flask
from flask_migrate import Migrate
from .models import db
from .config import Config
from .controllers import restaurant_controller, pizza_controller, restaurant_pizza_controller



migrate=Migrate()

def create_my_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)


    return app



# if __name__ =='__main__':
#      app.run(debug= True, port = 4000)
#     # with app.app_context():
#     #     db.create_all()
#     #     app.run(debug =True)
