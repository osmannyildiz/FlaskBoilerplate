from flask import Flask
from flask_boilerplate import config


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(config.FLASK_CONFIG)
    app.secret_key = config.FLASK_SECRET_KEY

    from flask_boilerplate.blueprints.main.views import bp_main
    app.register_blueprint(bp_main)
    from flask_boilerplate.blueprints.api_main.views import bp_api_main
    app.register_blueprint(bp_api_main, url_prefix="/api/main")

    return app
