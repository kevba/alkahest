from sqlalchemy import inspect, ForeignKey
from alkahest.utils import snake_case_string


class Alkahest(object):
    columns_blacklist = ['id']

    def to_dict(self, cascading=True):
        dict_ = {}
        model = inspect(self)

        columns = [c for c in model.mapper.columns.values()
                   if c.key not in self.columns_blacklist]

        # Remove foreignkeys, because tehy'll get a nested dict
        if cascading:
            columns = [c for c in columns if len(c.foreign_keys) == 0]

        for col in columns:
            if col.key not in self.columns_blacklist:
                dict_[col.key] = getattr(self, col.key)

        if cascading:
            for rel_attr in model.mapper.relationships.keys():
                dict_[rel_attr] = getattr(self, rel_attr).to_dict(
                    cascading=False
                )

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
