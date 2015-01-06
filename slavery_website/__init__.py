from flask import flask
from cms.views import cms

app = Flask(__name__)
app.register_blueprint(cms, url_prefix='/admin') 