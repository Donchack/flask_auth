from flask import Flask
from flask_login import LoginManager

from .classes import User


users = []
users.append(User(1, 'Admin', '1111'))
users.append(User(2, 'User1', '4321'))

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['DEBUG'] = 'True'
    
    login_mangr = LoginManager()
    login_mangr.init_app(app)
    @login_mangr.user_loader
    def load_user(user_id):
        for user in users:
            if user_id == user.id:
                return user

    from .main import main as main_bluepr
    app.register_blueprint(main_bluepr)

    from .auth import auth as auth_bluepr
    app.register_blueprint(auth_bluepr)

    return app