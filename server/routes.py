from flask import current_app as app
from flask import render_template, url_for, redirect
from .models import Pattern

from .forms import PatternForm

@app.route("/")
def home():
    """Landing page."""
    return render_template(
        'home.html',
        title="Welcome to Pattern Finder!",
        description="A website to find interesting correlations in data."
    )

@app.route("/patterns/new", methods=["GET", "POST"])
def new_pattern():
    """Landing page."""
    form = PatternForm()
    if form.validate_on_submit():
        print("test thing")
        name = form.name.data
        return redirect(url_for("pattern", name=name))
    else:
        print("other thing")
    return render_template(
        'newpattern.html',
        form=form,
    )

#this url is going to change once we start db/user stuff; for now it'll stay like this
@app.route("/patterns/<name>", methods=["GET", "POST"])
def pattern(name):
    """Landing page."""
    return render_template(
        'pattern.html',
        pattern = Pattern(name=name, patterns=["bop", "q", "17"], datapoints=["absolutely nothing"])
    )