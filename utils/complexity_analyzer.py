import time

def analyze_complexity(func, *args, **kwargs):
    """
    Measures the execution time of a given function.
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"[{func.__name__}] Execution time: {execution_time:.6f} seconds")
    return result
