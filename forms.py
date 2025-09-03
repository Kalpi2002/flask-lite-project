# forms.py
from flask_wtf import FlaskForm

class DeleteForm(FlaskForm):
    # no fields needed; we only use CSRF token provided by FlaskForm
    pass
