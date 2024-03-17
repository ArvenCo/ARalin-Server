from libs import *

from src.routes.web import web
from src.models import db

app = Flask(__name__)

def main():
    
    app.config.update({
        'SQLALCHEMY_DATABASE_URI' : 'sqlite:///aralin.db'
    })
    
    app.register_blueprint(web)
    db.init_app(app)

    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    main()
    app.run(debug=True, )