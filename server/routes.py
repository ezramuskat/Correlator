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
        #temp test data for datapoints until we add the logic to the PatternSet class
        return redirect(url_for("main_bp.pattern_preview", pattern_set = PatternSet(name=form.name.data, patterns=form.patterns.data, datapoints=["absolutely nothing"])))
    else:
        print("other thing")
    return render_template(
        'newpattern.html',
        form=form,
    )

#this url is used as a preview for the pattern set
#logged in users can save the pattern set
#logged out users will still be able to see it
@main_bp.route("/patterns/<pattern_set>", methods=["GET", "POST"])
def pattern_preview(pattern_set):
    """Landing page."""
    return render_template(
        'pattern.html',
        
        patternset = pattern_set
        #patternset = PatternSet(name=name, patterns=["bop", "q", "17"], datapoints=["absolutely nothing"])
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

