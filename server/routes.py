from flask import current_app as app
from flask import render_template

@app.route("/")
def home():
    """Landing page."""
    return render_template(
        'home.html',
        title="Home page",
        description="A website to find interesting correlations in data."
    )