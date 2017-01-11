from functools import wraps

from flask import abort, current_app as app
from alkahest.mixin import Alkahest


def get_resource_class(func):
    """ Wraps an endpoint that gets a resource name as parameter and
    returns a resource class based on that. If no such resource can be found it
    aborts with a 404 status code
    """
    @wraps(func)
    def wrapper(resource_name):
        resource_class = find_class(resource_name)
        if resource_class is None:
            abort(404)
        return func(resource_class)
    return wrapper


def get_resource_object(func):
    """ Wraps an endpoint that gets a resource name + id as parameter and
    returns a resource object based on those. If no such resource can be found
    it aborts with a 404 status code
    """
    @wraps(func)
    def wrapper(resource_name, id):
        resource_class = find_class(resource_name)
        if resource_class is None:
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
    # NOTE: Only direct children are allowed. THis is to prevent accidently
    # exposing data that should be exosed
    for klass in Alkahest._get_subclasses():
        if klass._get_resource_name() == resource_name:
            return klass
    # Maybe too verbose.
    return None
