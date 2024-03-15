from libs import *

web = Blueprint('web', __name__)

@web.route('/')
def index():
    return render_template('index.html')

@web.route('/login')
def login():
    return render_template('auth/login.html')