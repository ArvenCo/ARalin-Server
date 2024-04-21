from libs import LoginManager, Bcrypt, request, login_user, logout_user, redirect, url_for
from src.models import User, db

login_manager = LoginManager()
login_manager.login_view = "web.login"
bcrypt = Bcrypt()

@login_manager.user_loader
def user_loader(id):
    return User.query.get(id)

class AuthController():

    def users():
        users = User.query.filter(User.id != 1).all()
        return users
    
    def login():
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('web.index'))
        
        return redirect(url_for('web.login'))

    def signup(username, password, confirm_password):
        # username = request.form.get('username')
        # password = request.form.get('password')
        # confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(username=username).first()
        if user is None and password == confirm_password:
            user = User(username=username, password=bcrypt.generate_password_hash(password))
            db.session.add(user)
            db.session.commit()

            login_user(user)
            return True
        return False

    def logout():
        logout_user()
        return redirect(url_for('web.login'))
    
    def create_admin():
        if User.query.count() == 0:
            user = User(username="supderadmin", password=bcrypt.generate_password_hash("aclcButuan2024"))
            db.session.add(user)
            db.session.commit()