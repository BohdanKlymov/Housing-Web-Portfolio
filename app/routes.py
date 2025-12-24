from flask import Blueprint, render_template, redirect, url_for, session, request, send_from_directory
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

from .models import User
from .translations import translations

main = Blueprint("main", __name__)

def get_language():
    return session.get("lang", "en")


@main.route("/set-language/<code>")
def set_language(code):
    if code in ("en", "de"):
        session["lang"] = code
    return redirect(request.referrer or url_for("main.index"))

@main.route("/")
def index():
    lang = get_language()
    return render_template(
        "index.html",
        t=translations[lang],
        lang=lang
    )


@main.route("/login", methods=["GET", "POST"])
def login():
    lang = get_language()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("main.index"))

    return render_template(
        "login.html",
        t=translations[lang],
        lang=lang
    )


@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@main.route("/chat")
@login_required
def chat():
    lang = get_language()
    return render_template(
        "chat.html",
        t=translations[lang],
        lang=lang
    )


@main.route("/documents/<path:filename>")
@login_required
def documents(filename):
    return send_from_directory("documents", filename)

@main.route("/impressum")
def impressum():
    lang = get_language()
    return render_template(
        "impressum.html",
        t=translations[lang],
        lang=lang
    )


@main.route("/privacy")
def privacy():
    lang = get_language()
    return render_template(
        "privacy.html",
        t=translations[lang],
        lang=lang
    )
