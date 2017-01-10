def camel_case_string(string):
    """ Turns a snake-cased string into a camel-cased one

    :param string: snake-cased string
    :returns: camel-cased string.
    """
    camel_cased = ''
    for word in string.split('_'):
        camel_cased += word.capitalize()

    return camel_cased


class Alkahest(object):
    columns_blacklist = ['id']
    resource_name = camel_case_string(__name__)

    def to_dict(self):
        dict_ = {}

        for name in self. _get_column_names():
            if name not in self.columns_blacklist:
                dict_[name] = getattr(self, name)

        return dict_

    def _get_column_names(self):
        return [column.name for column in self.__table__.columns]
