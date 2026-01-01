from flask import Blueprint, render_template, send_from_directory, current_app

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/documents/<path:filename>")
def documents(filename):
    return send_from_directory(
        current_app.root_path + "/documents",
        filename,
        as_attachment=False
    )
