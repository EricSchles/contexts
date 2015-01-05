from flask import Flask, current_app

app = Flask(__name__)

with app.app_context():
	print current_app.name