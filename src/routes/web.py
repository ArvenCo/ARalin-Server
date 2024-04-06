from libs import *
from src.controller.project import ProjectController

web = Blueprint('web', __name__)

@web.route('/')
def index():
    
    return ProjectController.index()

@web.route('/login')
def login():
    return render_template('auth/login.html')

@web.route('/project', methods=['POST'])
def project():
    ProjectController.store()
    return redirect(url_for('web.index'))


@web.route('/generate/<data>')
def generate(data):
    return ProjectController.gerate_qr(data)

@web.route('/images')
def images():
    id = request.args.get('id')
    images = []
    for file in ProjectController.get_images(id):
        images.append( url_for('static', filename=f'uploads/{id}/images/{file}'))
    return jsonify(images)

