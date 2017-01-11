def camel_case_string(string):
    """ Turns a snake-cased string into a camel-cased one

    :param string: snake-cased string
    :returns: camel-cased string.
    """
    camel_cased = ''
    for word in string.split('_'):
        camel_cased += word.capitalize()

    return camel_cased
