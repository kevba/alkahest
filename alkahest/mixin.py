from alkahest.utils import snake_case_string


class Alkahest(object):
    columns_blacklist = ['id']

    # __metaclass__ = AlkahestMetaClass
    def to_dict(self):
        dict_ = {}

        for name in self. _get_column_names():
            if name not in self.columns_blacklist:
                dict_[name] = getattr(self, name)

        return dict_

    def _get_column_names(self):
        return [column.name for column in self.__table__.columns]

    @classmethod
    def _get_subclasses(cls):
        """ Return a generator of all direct subclasses
        """
        for subclass in cls.__subclasses__():
            yield subclass

    @classmethod
    def _get_resource_name(cls):
        """ Checks if a resource name has been defined on the class. If no name
        has been defined it uses a snae-cased version of the classname.

        :returns: String resource_name
        """
        rsn = ''
        try:
            rsn = cls.resource_name
        except AttributeError:
            rsn = snake_case_string(cls.__name__)
        return rsn
