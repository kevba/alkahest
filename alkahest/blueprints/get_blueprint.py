from flask import Blueprint, abort, jsonify, current_app as app
from alkahest.wrappers import get_resource_class, get_resource_object

bp = Blueprint('alkahest_get', __name__)


@bp.route('/<resource_name>', methods=['GET'])
@get_resource_class
def get_resource(resource_class):
    resources = app.session.query(resource_class).all()
    return jsonify({'data': [r.to_dict() for r in resources]})


@bp.route('/<resource_name>/<int:id>', methods=['GET'])
@get_resource_object
def get_resource_by_id(resource_object):
    return jsonify(resource_object.to_dict())


@bp.route('/wow', methods=['GET'])
def wow():
    abort(418)
