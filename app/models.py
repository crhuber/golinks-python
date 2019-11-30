from flask import current_app, request, url_for
from datetime import datetime
from . import db


class GoLink(db.Model):
    __tablename__ = 'golink'
    # id = db.Column(db.Integer, primary_key=True)
    destination_url = db.Column(db.String(300))
    keyword = db.Column(db.String(300), primary_key=True)
    keyword_prefix = db.Column(db.String(300))
    description = db.Column(db.String(300))
    date_added = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    views = db.Column(db.Integer())
