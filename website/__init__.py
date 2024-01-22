from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_socketio import SocketIO, send

db = SQLAlchemy()
DB_NAME = "database.db"
app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins="*")

def create_app():


        

    app.config['SECRET_KEY'] = "hellasdo jspa ojdioashdiOAHWUUHFUSA ND OAISHD UWHETUDSH89WY3Q89WYQ389WURHworld"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME
    app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024    # 50 Mb limit
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)



    from .views import views
    #from .models import User,adminAccount



    create_database(app)


    app.register_blueprint(views, url_prefix="/")


    return app



def create_socketio():
    return socketio    


def create_database(app):
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created database!")