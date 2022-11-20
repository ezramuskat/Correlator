from flask_login import login_required, logout_user, current_user, login_user
from .models import db, User
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None