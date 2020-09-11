class store_results:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        with open('results.txt', 'a') as file:  # context manager
            file.write(f"Function '{self._func.__name__}' was add called. "
                       f"Result: {self._func(*args, **kwargs)}\n")
