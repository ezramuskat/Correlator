from flask import current_app as app
from flask import render_template, url_for, redirect, Blueprint
from flask_login import current_user, login_required
from .models import Pattern

from .forms import PatternForm

main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@main_bp.route("/")
def home():
    """Landing page."""
    return render_template(
        'home.html',
        title="Welcome to Pattern Finder!",
        description="A website to find interesting correlations in data."
    )

@main_bp.route("/patterns/new", methods=["GET", "POST"])
def new_pattern():
    """Landing page."""
    form = PatternForm()
    if form.validate_on_submit():
        print("test thing")
        name = form.name.data
        return redirect(url_for("main_bp.pattern", name=name))
    else:
        print("other thing")
    return render_template(
        'newpattern.html',
        form=form,
    )

#this url is going to change once we start db/user stuff; for now it'll stay like this
@main_bp.route("/patterns/<name>", methods=["GET", "POST"])
def pattern(name):
    """Landing page."""
    return render_template(
        'pattern.html',
        pattern = Pattern(name=name, patterns=["bop", "q", "17"], datapoints=["absolutely nothing"])
    )

@main_bp.route("/account", methods=["GET", "POST"])
@login_required
def account():
    return render_template(
        'account.html',
        title='account page',
        user=current_user,
        body="You are now logged in!"
    )