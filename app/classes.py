from flask_login import UserMixin
from werkzeug.security import generate_password_hash

# наследование от UserMixin добавляет дефолтные методы для работы с flask_login
class User(UserMixin):
    def __init__(self, id:int, user_name:str, password:str):
        self.id = id
        self.user_name = user_name
        self.psw_hash = generate_password_hash(password)
    
    def __repr__(self) -> str:
        return f'{self.id}:{self.user_name}'