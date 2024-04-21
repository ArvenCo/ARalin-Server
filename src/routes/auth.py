from libs import Blueprint, request, redirect
from src.controller.auth import AuthController
auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('login', methods=['POST'])
def login():
    return AuthController.login()

@auth.route('logout', methods=['POST'])
def logout():
    return AuthController.logout()

@auth.route('register-user', methods=['POST'])
def register():
    registered = AuthController.signup(
        request.form['username'], 
        request.form['password'],
        request.form['confirm_password'])
    
    return redirect(request.referrer)

