from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# наследование от UserMixin добавляет дефолтные методы для работы с flask_login
class User(UserMixin):
    def __init__(self, id: int, user_name: str, password: str):
        self.__id = id
        self.user_name = user_name
        self.__psw_hash = generate_password_hash(password)
    
    def check_password(self, password: str) -> bool:
        return check_password_hash(self.__psw_hash, password)

    def get_id(self) -> int:
        return self.__id

    def __repr__(self) -> str:
        return f'{self.__id}:{self.user_name}'