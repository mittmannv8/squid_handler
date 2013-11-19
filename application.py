# -*- coding: utf-8 -*-

from flask import (
        Flask, redirect, url_for, render_template
        )
from flask.ext.babel import Babel

babel = Babel()

# Application Factories: http://flask.pocoo.org/docs/patterns/appfactories/
def create_app(config_filename):
    # Create the app instance and define default settings
    app = Flask(__name__)
    app.config.from_object(config_filename)

    # Register extensions
    babel.init_app(app)

    # Import and register blueprints
    from report.app import report_app
    app.register_blueprint(report_app, url_prefix='/reports')

    # Routes and http handlers
    @app.route('/')
    def index():
        return redirect(url_for('report_app.index'), code=302)

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('403.html'), 403

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('500.html'), 500

    return app
