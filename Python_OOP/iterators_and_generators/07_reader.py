def read_next(*args):
    for c in args:
        for x in c:
            yield x
