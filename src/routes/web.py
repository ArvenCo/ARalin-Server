from libs import *

web = Blueprint('web', __name__)

@web.route('/')
def index():
    return render_template('index.html')