import time
from multiprocessing import Pool

def cpu_heavy_task(n):
    return sum(i * i for i in range(n))

def run_synchronous(numbers):
    return [cpu_heavy_task(n) for n in numbers]

def run_multiprocessing(numbers):
    with Pool() as pool:
        return pool.map(cpu_heavy_task, numbers)

if __name__ == "__main__":
    numbers = [10_000_000, 10_000_000, 10_000_000, 10_000_000]

    start = time.perf_counter()
    run_synchronous(numbers)
    sync_time = time.perf_counter() - start

    start = time.perf_counter()
    run_multiprocessing(numbers)
    mp_time = time.perf_counter() - start

    print("Synchronous time:", sync_time, "seconds")
    print("Multiprocessing time:", mp_time, "seconds")