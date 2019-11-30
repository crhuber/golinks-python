#!/usr/bin/env python
import os
from app import create_app, db
from app.models import GoLink
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
cors = CORS(app, resources={r"/api/*": {"origins": app.config['CORS_ORIGIN']}})
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, GoLink=GoLink)


if __name__ == '__main__':
    manager.run()
