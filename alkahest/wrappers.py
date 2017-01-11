from functools import wraps

from flask import abort, current_app as app
from alkahest.mixin import Alkahest
from alkahest.utils import camel_case_string


def get_resource_class(func):
    @wraps(func)
    def wrapper(resource_name):
        resource_class = find_class(resource_name)
        if resource_class is None:
            # This resource does nor exist
            abort(404)
        return func(resource_class)
    return wrapper


def get_resource_object(func):
    @wraps(func)
    def wrapper(resource_name, id):
        resource_class = find_class(resource_name)
        if resource_class is None:
            # This resource does not exist
            abort(404)

        obj = app.session.query(resource_class).filter_by(id=id).first()
        if obj is None:
            abort(404)

        return func(obj)
    return wrapper


def find_class(resource_name):
    """ returns a class with a matching resource name, or None if no class can
    be found.

    :resource_name: String indetifing resource.
    :returns: A class.
    """
    # look for the model in the subclasses of Alkahest
    for klass in Alkahest._get_subclasses():
        if klass._get_resource_name() == camel_case_string(resource_name):
            return klass
    # Maybe too verbose.
    return None
