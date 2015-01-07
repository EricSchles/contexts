from flask import Blueprint, render_template
from models import *
logger = Blueprint('logger',__name__,template_folder="templates")

@logger.route("/page_views",methods=["GET","POST"])
def page_views():
	pages = get_page_views()
	return render_template("viewer.html",pages=pages)

@logger.route("/button_press", methods=["GET","POST"])
def button_press():
	buttons = get_button_press()
	return render_template("viewer.html",buttons=buttons)

@logger.route("/comments/<user>", methods=["GET","POST"])
@logger.route("/comments", methods=["GET","POST"])
def comments(user=None):
	if user:
		user_comments = get_user_comments()
		users = get_users()
		return render_template("viewer.html", user_comments = user_comments, users = users)
	else:
		users = get_users()
		return render_template("viewer.html",user_comments = "No user selected", users=users)
	#if you don't know the username you want to see comments for 
	#then what happens instead is a list of users is returned with
	#links to the specific user.  Clicking on an individual user
	#should call the method again for the individual user.

@logger.route("/messages/<user>", methods=["GET","POST"])
@logger.route("/messages", methods=["GET","POST"])
def messages(user=None):
	if user:
		user_messages = get_user_messages()
		users = get_users()
		return render_template("viewer.html", user_messages = user_comments, users = users)
	else:
		users = get_users()
		return render_template("viewer.html",user_messages = "No user selected", users=users)
	#if you don't know the username you want to see comments for 
	#then what happens instead is a list of users is returned with
	#links to the specific user.  Clicking on an individual user
	#should call the method again for the individual user.

