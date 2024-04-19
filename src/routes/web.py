from libs import *
from src.controller.project import ProjectController
from src.controller.auth import AuthController
web = Blueprint('web', __name__)

@web.route('/')
@login_required
def index():
    return ProjectController.index()

@web.route('/login')
def login():
    AuthController.create_admin()
    return render_template('auth/login.html')

@web.route('/project', methods=['POST'])
@login_required
def project():
    ProjectController.store()
    return redirect(url_for('web.index'))

@web.route('/edit/<id>', methods=['POST', 'GET'])
def edit(id):
    if request.method == 'POST':
        return ProjectController.update(id)
    return ProjectController.show(id=id)

@web.route('/delete/<id>', methods=['POST'])
def delete(id):
    return ProjectController.delete(id=id)

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

