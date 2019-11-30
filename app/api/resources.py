from flask_restful import Resource, fields, marshal_with, marshal, inputs
from ..models import GoLink
from flask_restful import reqparse, abort
from .. import db
import re
from sqlalchemy import desc

golink_fields = {
    'destination_url': fields.String,
    'date_added': fields.DateTime(dt_format='iso8601'),
    'keyword': fields.String,
    'description': fields.String,
    'views': fields.Integer
}

def abort_unmatched_placeholders(keyword, destination_url):
    if keyword.count("%") != destination_url.count("%"):
        abort(400, message="placeholders must match on destination and keyword")
    


def abort_empty_string(s):
    if not s:
        abort(400, message="empty fields are not allowed")


def clean_keyword(keyword):
    if not keyword[0].isalpha():
        return keyword[1:]
    return keyword


def abort_if_banned(keyword):
    banned_keywords = ["/", ".", "api", "healthz",
                       "version", "links", "edit", "delete", "directory"]
    if keyword in banned_keywords:
        abort(400, message="this keyword is not allowed: {}".format(keyword))


def unique_keyword(keyword):
    """Return keyword if valid, raise an exception in other case."""
    go_link = GoLink.query.get(keyword)
    if not go_link:
        return keyword
    else:
        raise ValueError('keyword must be unique')


def abort_if_not_unique(keyword):
    go_link = GoLink.query.get(keyword)
    if go_link:
        abort(400, message="link name must be unique {}".format(keyword))


def update_stats(golink):
    # update stats
    views = golink.views
    if views is None:
        views = 1
    else:
        views += 1
    golink.views = views
    db.session.commit()


# parsers
golink_parser = reqparse.RequestParser()
golink_parser.add_argument(
    'destination_url', required=True, type=inputs.url, location='json', nullable=False)
golink_parser.add_argument('keyword', required=True,
                           type=unique_keyword, location='json', nullable=False)
golink_parser.add_argument('description', required=False,
                           help='description is optional', type=str, location='json')

golink_put_parser = reqparse.RequestParser()
golink_put_parser.add_argument(
    'destination_url', required=True, type=inputs.url, location='json')
golink_put_parser.add_argument('description', required=False,
                               help='description is optional', type=str, location='json')
# search
search_parser = reqparse.RequestParser()
search_parser.add_argument('q', type=str, location='args')

class GoLinkGroupList(Resource):

    def get(self, prefix):
        golinks = GoLink.query.filter_by(keyword_prefix=prefix).limit(100).all()
        if golinks:
            golinks = [marshal(golink, golink_fields) for golink in golinks]
            return {"results": golinks}, 200
        else:
            abort(404)


class GoLinkDetail(Resource):

    @marshal_with(golink_fields)
    def get(self, keyword):
        golink = GoLink.query.get(keyword)
        if golink:
            update_stats(golink)
            return golink
        else:
            # handle programatic links
            # ie: gh/%s pointing > https://github.com/%s
            golinks = GoLink.query.filter_by(keyword_prefix=keyword.split('/')[0]).all()
            if golinks:
                for golink in golinks:
                    if "%s" in golink.keyword:
                        # see if incoming keyword has a slash
                        if "/" in keyword:
                            update_stats(golink)
                            placeholder = keyword.split('/')[1]
                            programmatic_url = golink.destination_url.replace("%s", placeholder, 1)
                            # make a duplicate object since the db was being overwritten with temp url
                            golink_temp = {}
                            golink_temp['destination_url'] = programmatic_url
                            golink_temp['keyword'] = golink.keyword
                            golink_temp['views'] = golink.views
                            golink_temp['description'] = golink.description
                            golink_temp['date_added'] = golink.date_added
                            return golink_temp
                        else:
                            abort(404)
                    else:
                        abort(404)
            else:
                abort(404)



    def delete(self, keyword):
        golink = GoLink.query.get(keyword)
        if not golink:
            abort(404)
        db.session.delete(golink)
        db.session.commit()
        return {
            "message": "ok",

        }, 204

    @marshal_with(golink_fields)
    def put(self, keyword):
        args = golink_put_parser.parse_args(strict=True)
        golink = GoLink.query.get(keyword)
        if not golink:
            abort(404)
        golink.destination_url = args.destination_url
        golink.description = args.description
        db.session.commit()
        return {
            "message": "ok",

        }, 201


class GoLinkList(Resource):

    # @marshal_with(golink_fields, envelope='results')
    def get(self):
        golinks = GoLink.query.order_by(desc('date_added')).limit(100)
        golinks = [marshal(golink, golink_fields) for golink in golinks]
        return {"results": golinks}, 200

    @marshal_with(golink_fields)
    def post(self):
        args = golink_parser.parse_args(strict=True)
        abort_empty_string(args.keyword)
        abort_if_banned(args.keyword)
        keyword = clean_keyword(args.keyword)
        if "%" in args.keyword:
            abort_unmatched_placeholders(args.keyword, args.destination_url)
        golink = GoLink(destination_url=args.destination_url,
                        keyword=keyword, 
                        description=args.description,
                        keyword_prefix=keyword.split('/')[0]
            )
        db.session.add(golink)
        db.session.commit()
        return golink, 201


class Search(Resource):

    def get(self):
        args = search_parser.parse_args(strict=True)
        golinks = GoLink.query.filter(GoLink.keyword.ilike('%{}%'.format(args.q))).limit(50).all()   
        golinks = [marshal(golink, golink_fields) for golink in golinks]
        return {"results": golinks}, 200

class Health(Resource):

    def get(self):
        return 200