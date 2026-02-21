import functools

debug_count = 0
stop_debug_count = 20
def debug(func):
    global debug_count
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global debug_count
        result = func(*args, **kwargs)
        if debug_count < stop_debug_count:
            print(f"Called function {func.__name__}\tArgs: {args}\tKwargs: {kwargs}\tReceived output {result}"[:200])
            debug_count += 1
        return result
    return wrapper

def debug_methods(cls):
    # return
    for name, attr in vars(cls).items():
        # Check if the attribute is a function (method)
        if callable(attr):
            setattr(cls, name, debug(attr))
    return cls
