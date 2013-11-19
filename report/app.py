# -*- coding: utf-8 -*-
from flask import Blueprint
from views import *

# Create report_app as blueprint
report_app = Blueprint('report_app', __name__)

# Routes
report_app.add_url_rule('/', 'index', index)
