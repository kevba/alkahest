# from collections import defaultdict


# class AlkahestMetaClass(type):
#         __inheritors__ = defaultdict(list)
#
#         def __new__(meta, name, bases, dict_):
#             klass = type.__new__(meta, name, bases, dict_)
#             for base in klass.mro()[1:-1]:
#                 meta.__inheritors__[base].append(klass)
#             return klass
#
#         def __init__(cls, classname, bases, dict_):
#             return super(AlkahestMetaClass, cls).__init__(
#                 classname, bases, dict_
#             )

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
        for subclass in cls.__subclasses__():
            # yield from subclass.get_subclasses()
            yield subclass

    @classmethod
    def _get_resource_name(cls):
        rsn = ''
        try:
            rsn = cls.resource_name
        except AttributeError:
            rsn = cls.__name__
        return rsn
