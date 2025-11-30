import time

def measure_time(func, arr):
    start = time.time()
    func(arr)
    end = time.time()
    return end - start
