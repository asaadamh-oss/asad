from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User
from app.forms import LoginForm

main = Blueprint("main", __name__)

@main.route("/")
def index():
    if current_user.is_authenticated:
        return f"<div dir='rtl' style='padding: 20px;'><h1>مرحباً {current_user.username}!</h1><a href='/logout'>تسجيل الخروج</a></div>"
    return redirect(url_for("main.login"))

@main.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("main.index"))
        else:
            flash("اسم المستخدم أو كلمة المرور غير صحيحة", "error")

    return render_template("login.html", form=form)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))
