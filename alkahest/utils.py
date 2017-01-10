import inspect
from functools import wraps

from flask import abort
from alkahest.mixin import Alkahest


def get_resource(func):
    @wraps(func)
    def wrapper(resource_name):
        # Capitalize the modelname. TODO: MAke configurable
        resource_class = find_class(resource_name)
        if resource_class is None:
            # This resource does nor exist
            abort(404)
        return resource_class
    return wrapper


def find_class(resource_name):
    """ returns a class with a matching resource name, or None if no class can
    be found.

    :resource_name: String indetifing resource.
    :returns: A class.
    """
    # look for the model in the subclasses of Alkahest
    for _, obj in inspect.getmembers(Alkahest):
        if obj.resource_name == resource_name:
            return obj
    # Maybe too verbose.
    return None
