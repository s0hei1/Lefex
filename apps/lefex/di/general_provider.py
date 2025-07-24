from typing import ClassVar, Any
from typing import TypeVar
from apps.lefex.config import Settings
from hashlib import sha224


class DependencyProvider(object):

    _objects : ClassVar[dict[type, Any]] = {}


    @classmethod
    def settings(cls) -> Settings:

        if Settings not in cls._objects:
            cls._objects[Settings] = Settings()
            return cls._objects[Settings]
        else:
            return cls._objects[Settings]

    #
    # _classes : ClassVar[dict[str, dict]] = {}
    # @classmethod
    # def add_dependency(cls, clazz : type,*args, **kwargs):
    #
    #     class_and_params = {
    #         "class_name" : clazz,
    #         "args" : args,
    #         "kwargs" : kwargs,
    #     }
    #
    #     result = sha224(str(class_and_params).encode()).hexdigest()
    #
    #     cls._classes[result] = class_and_params
    #
    #     return result
    #
