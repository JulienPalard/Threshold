import functools

def knock_door(argument_items):
    def _knock_door(method):
        @functools.wraps(method)
        def _wrapper(*args, **kwargs):
            print(argument_items[0].name)
            return method(*args, **kwargs)
        return _wrapper
    return _knock_door
