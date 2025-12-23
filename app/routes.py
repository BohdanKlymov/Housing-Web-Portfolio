from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Message
from . import db
from flask import session
from .translations import translations

def get_language():
    return session.get("lang", "de")

main = Blueprint("main", __name__)


@main.route("/")
def index():
    lang = get_language()
    return render_template(
        "index.html",
        t=translations[lang],
        lang=lang
    )



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
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()
        if user and check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("main.chat"))
    return render_template("login.html")


@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@main.route("/chat", methods=["GET", "POST"])
@login_required
def chat():
    if request.method == "POST":
        msg = Message(
            user_id=current_user.id,
            sender="user",
            content=request.form["message"]
        )
        db.session.add(msg)
        db.session.commit()

    messages = Message.query.filter_by(user_id=current_user.id).order_by(
        Message.timestamp.asc()
    ).all()

    return render_template("chat.html", messages=messages)


@main.route("/lang/<code>")
def set_language(code):
    if code in ["de", "en"]:
        session["lang"] = code
    return redirect(url_for("main.index"))

