from app.models.user import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class LoginService:
    def create_user(self,username, password):
        password_hash = generate_password_hash(password)
        user = User(username=username, password=password_hash)
        db.session.add(user)
        db.session.commit()
        return user

    def get_user_by_username(self,username):
        return User.query.filter_by(username=username).first()

    def verify_password(self,user, password):
        return check_password_hash(user.password, password)