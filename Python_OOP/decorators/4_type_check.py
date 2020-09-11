def type_check(arg_type):
    def decorator(func):
        def wrapper(x):
            if isinstance(x, arg_type):
                return func(x)
            return "Bad Type"
        return wrapper
    return decorator
