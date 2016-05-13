import functools

def knock_door(argument_item):
    def _knock_door(method):
        @functools.wraps(method)
        def _wrapper(self, *args, **kwargs):
            return _wrapper
        return _knock_door
