from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import config
db = SQLAlchemy()

from .api.resources import GoLinkDetail, GoLinkList, GoLinkGroupList, Search, Health

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    from .api import api as api_blueprint
    api = Api(api_blueprint)

    # routes
    api.add_resource(GoLinkList, '/links')
    # note <path> has special significance in that it matches after slashes
    api.add_resource(GoLinkDetail, '/links/<path:keyword>',
                     endpoint='golink_detail')
    api.add_resource(GoLinkGroupList, '/group/<path:prefix>',
                     endpoint='golinkgroup_list')
    api.add_resource(Search, '/search',
                     endpoint='search')
    api.add_resource(Health, '/healthz',
                     endpoint='health')
    app.register_blueprint(api_blueprint, url_prefix='/api')
    return app
