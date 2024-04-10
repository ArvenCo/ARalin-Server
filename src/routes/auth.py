from libs import Blueprint, request
from src.controller.auth import AuthController
auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('login', methods=['POST'])
def login():
    return AuthController.login()

@auth.route('logout', methods=['POST'])
def logout():
    return AuthController.logout()


