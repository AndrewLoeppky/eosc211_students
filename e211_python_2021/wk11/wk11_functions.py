def timeit(method):
    """
    https://www.laurivan.com/braindump-use-a-decorator-to-time-your-python-function/
    """
    import time
    
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        elapsed = te - ts

        # print(f'time to generate plot: {elapsed}s')
        return f"time to run function: {elapsed} sec"

    return timed