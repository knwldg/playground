import time


def time_function_ns(func, *args):
    start_time = time.perf_counter_ns()
    result = func(*args)
    print(f"{time.perf_counter_ns() - start_time} ns")
    return result
