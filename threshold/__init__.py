import functools
from threshold.filter import Filter

def knock_door(argument_items):
    def _knock_door(method):
        @functools.wraps(method)
        def _wrapper(self, *args, **kwargs):
            kwargs["params"] = Filter(argument_items, self)()
            return method(self, *args, **kwargs)
        return _wrapper
    return _knock_door
