from libs import *

from src.routes.web import web
from src.routes.auth import auth
from src.routes.stream import stream
from src.models import db
from src.controller.auth import login_manager, bcrypt

app = Flask(__name__)

def main():
    
    app.config.update({
        'SQLALCHEMY_DATABASE_URI' : 'sqlite:///aralin.db',
    })
    app.secret_key = "SuperSecretKey"
    
    app.register_blueprint(web)
    app.register_blueprint(auth)
    app.register_blueprint(stream)
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    main()
    app.run(debug=True, )