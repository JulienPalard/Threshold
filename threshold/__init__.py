import functools
from threshold.filter import Filter

def knock_door(argument_items, request_config_class):
    def _knock_door(method):
        @functools.wraps(method)
        def _wrapper(self, *args, **kwargs):
            kwargs["params"] = Filter(argument_items, self, request_config_class)()
            return method(self, *args, **kwargs)
        return _wrapper
    return _knock_door
