import re


def camel_case_string(string):
    """ Turns a snake-cased string into a camel-cased one

    :param string: snake-cased string
    :returns: camel-cased string.
    """
    camel_cased = ''
    for word in string.split('_'):
        camel_cased += word.capitalize()

    return camel_cased


def snake_case_string(string):
    """ Turns a camel-cased string into a snake-cased one

    :param string: camel-cased string
    :returns: snake-cased string.
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
