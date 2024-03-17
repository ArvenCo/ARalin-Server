from libs import *
from src.controller.project import store

web = Blueprint('web', __name__)

@web.route('/')
def index():
    return render_template('index.html')

@web.route('/login')
def login():
    return render_template('auth/login.html')

@web.route('/project', methods=['POST'])
def project():
    store()
    return redirect(url_for('web.index'))