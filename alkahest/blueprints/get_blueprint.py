from flask import Blueprint, jsonify, current_app as app
from alkahest.utils import get_resource

bp = Blueprint('alkahest_get', __name__)


@bp.route('/<resource_name>', methods=['GET'])
@get_resource
def get_resource(resource_class):
    resources = app.session.query(resource_class).all()
    return jsonify({'data': [r.to_dict() for r in resources]})
