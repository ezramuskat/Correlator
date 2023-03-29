from flask import current_app as app
from flask import render_template, url_for, redirect, Blueprint
from flask_login import current_user, login_required
from .models import PatternSet

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
        if current_user.is_authenticated:
            return redirect(url_for("main_bp.patternset", user=current_user.username, name=name))
        return redirect(url_for("main_bp.pattern_preview", user="default", name=name))
    else:
        print("other thing")
    return render_template(
        'newpattern.html',
        form=form,
    )

@main_bp.route("/<user>/patterns/<name>", methods=["GET", "POST"])
@login_required
def patternset(user, name):
    """Landing page."""
    return render_template(
        'pattern.html',

        patternset = PatternSet(name=name, patterns=["bop", "q", "17"], datapoints=["absolutely nothing"])
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

