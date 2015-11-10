# -*- coding: utf-8 -*-
from dynamic_preferences import global_preferences_registry


class Registry(object):
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = global_preferences_registry.manager()
        return cls._instance

    @property
    def instance(self):
        return self.get_instance()

    def __getitem__(self, key):
        return self.instance[key]


class LazySetting(object):
    def __init__(self, setting):
        registry = Registry()
        setattr(self, '__get_obj__', lambda: registry[setting])

    def __repr__(self):
        return self.__get_obj__().__str__()

    def __eq__(self, other):
        return self.__get_obj__() == other

    def __hash__(self):
        return hash(self.__get_obj__())


class LazyBooleanSetting(LazySetting):
    def __bool__(self):
        return self.__get_obj__()


class LazyStringSetting(str, LazySetting):

    def __getattr__(self, attr):
        string = self.__get_obj__()
        if hasattr(string, attr):
            return getattr(string, attr)
        raise AttributeError(attr)

    def to_json(self):
        return str(self.__get_obj__())

    def __repr__(self):
        return repr(self.__get_obj__())

    def __str__(self):
        return str(self.__get_obj__())

    def __len__(self):
        return len(self.__get_obj__())

    def __getitem__(self, key):
        return self.__get_obj__()[key]

    def __iter__(self):
        return iter(self.__get_obj__())

    def __contains__(self, item):
        return item in self.__get_obj__()

    def __add__(self, other):
        return self.__get_obj__() + other

    def __radd__(self, other):
        return other + self.__get_obj__()

    def __mul__(self, other):
        return self.__get_obj__() * other

    def __rmul__(self, other):
        return other * self.__get_obj__()

    def __lt__(self, other):
        return self.__get_obj__() < other

    def __le__(self, other):
        return self.__get_obj__() <= other

    def __eq__(self, other):
        return self.__get_obj__() == other

    def __ne__(self, other):
        return self.__get_obj__() != other

    def __gt__(self, other):
        return self.__get_obj__() > other

    def __ge__(self, other):
        return self.__get_obj__() >= other

__all__ = (
    'LazyBooleanSetting',
    'LazyStringSetting',
)
