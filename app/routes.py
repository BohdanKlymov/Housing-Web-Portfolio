from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    session,
    send_from_directory,
    abort
)
from flask_login import (
    login_user,
    login_required,
    logout_user,
    current_user
)
from werkzeug.security import generate_password_hash, check_password_hash
import os

from .models import User, Message
from .translations import translations
from . import db

main = Blueprint("main", __name__)


def get_language():
    return session.get("lang", "de")


@main.route("/")
def index():
    lang = get_language()
    return render_template(
        "index.html",
        t=translations[lang],
        lang=lang
    )


@main.route("/lang/<code>")
def set_language(code):
    if code in ["de", "en"]:
        session["lang"] = code
    return redirect(url_for("main.index"))


@main.route("/impressum")
def impressum():
    return render_template("impressum.html")


@main.route("/privacy")
def privacy():
    return render_template("privacy.html")


@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(
            name=request.form["name"],
            email=request.form["email"],
            password=generate_password_hash(request.form["password"])
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for("main.chat"))

    return render_template("register.html")


@main.route("/login", methods=["GET", "POST"])
def login():
    lang = get_language()
    ...
    return render_template("login.html", t=translations[lang], lang=lang)



@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@main.route("/chat", methods=["GET", "POST"])
@login_required
def chat():
    if request.method == "POST":
        message = Message(
            user_id=current_user.id,
            sender="user",
            content=request.form["message"]
        )
        db.session.add(message)
        db.session.commit()

    messages = Message.query.filter_by(
        user_id=current_user.id
    ).order_by(Message.timestamp.asc()).all()

    return render_template("chat.html", messages=messages)


@main.route("/documents/<filename>")
@login_required
def documents(filename):
    allowed_files = {
        "cv.pdf",
        "Internship_evaluation_24-25.pdf",
        "Grade_10_school_certificate_07-2025.pdf",
        "python2025_RecordOfAchievement.pdf"
    }

    if filename not in allowed_files:
        abort(404)

    docs_path = os.path.join(
        os.path.dirname(__file__),
        "documents"
    )

    return send_from_directory(docs_path, filename)
