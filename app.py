from libs import *

from src.routes.web import web

app = Flask(__name__)

def main():
    app.register_blueprint(web)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")