from timeit import default_timer as timer


def exec_time(func):
    def wrapper(*args, **kwargs):
        start_time = timer()
        func(*args, **kwargs)
        end_time = timer()
        execution_time = end_time - start_time
        return execution_time
    return wrapper
