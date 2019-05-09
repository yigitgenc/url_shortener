"""Application package."""

from typing import Union

from flask import Flask

from app.models import db
from app.views import RedirectView, ShortenView


def create_app(test_config: Union[dict, None] = None) -> Flask:
    """
    Creates application instance, configures and returns Flask app instance.
    Flask will automatically discover `create_app` function here.
    """
    # Create app instance.
    app = Flask(__name__)

    # If test_config provided, override the current config.
    if test_config:
        app.config.update(test_config)

    # Init SQLAlchemy.
    db.init_app(app)

    # Get default config variables from settings module.
    app.config.from_object('app.settings')

    # Set strict slashes to False in order use both types (ending with/without /).
    app.url_map.strict_slashes = False

    # Register endpoints.
    app.add_url_rule('/<string:code>', view_func=RedirectView.as_view('redirect_view'))
    app.add_url_rule('/shorten', view_func=ShortenView.as_view('shorten_view'))

    with app.app_context():
        db.create_all()

    return app
