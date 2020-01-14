from app.config.Application import GLOBAL_VALUE


class Api:

    def route(path, method):
        def wrapper(func):
            function_name = func.__qualname__.split('.')
            GLOBAL_VALUE[method+path] = {
                'class': function_name[0],
                'function': function_name[1]
            }
            return func
        return wrapper