from flask import Blueprint, render_template
from cms.models import *
cms = Blueprint("cms",__name__,template_folder='templates')

@cms.route("/admin/add",methods-["GET","POST"])
def add():
	return render_template("admin.html")

@cms.route("/admin/remove",methods=["GET","POST"])
def remove():
	return render_template("admin.html")

@cms.route("/admin/view_entries",methods=["GET","POST"])
def view_entries():
	entries = get_entries()
	return render_template("entries.html",entries=entries)