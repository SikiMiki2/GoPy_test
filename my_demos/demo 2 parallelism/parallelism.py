import time
from out import fast
import asyncio
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def count_range(start, limit, step):
    return sum(1 for n in range(start, limit, step) if is_prime(n))

#------------------------- plain python

def count_plain(limit):
    return count_range(0, limit, 1)

#------------------------- asyncio

async def worker(w, limit, workers):
    return count_range(w, limit, workers)

async def count_asyncio_main(limit, workers):
    parts = await asyncio.gather(*(worker(w, limit, workers) for w in range(workers)))
    return sum(parts)

def count_asyncio(limit, workers):
    return asyncio.run(count_asyncio_main(limit, workers))

#------------------------- threads

def count_threads(limit, workers):
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(count_range, w, limit, workers) for w in range(workers)]
        return sum(f.result() for f in futs)

#------------------------- processes

def count_processes(limit, workers):
    with ProcessPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(count_range, w, limit, workers) for w in range(workers)]
        return sum(f.result() for f in futs)

#------------------------- main part of the code

if __name__ == "__main__":
    LIMIT, WORKERS = 5_000_000, 8

    print(f"{LIMIT} numbers and {WORKERS} workers (threads/processes):")
    for name, fn, args in [
        ("plain",     count_plain,     (LIMIT,)),
        ("asyncio",   count_asyncio,   (LIMIT, WORKERS)),
        ("threads",   count_threads,   (LIMIT, WORKERS)),
        ("processes", count_processes, (LIMIT, WORKERS)),
        ("go 1 core (plain)",   fast.CountPrimes, (LIMIT, 1)),
        ("go same # of cores", fast.CountPrimes, (LIMIT, WORKERS)),
        ("go 19 cores", fast.CountPrimes, (LIMIT, 19)),
    ]:
        t = time.perf_counter()
        r = fn(*args)
        print(f"{name:20} {r}  {time.perf_counter() - t:.2f}s")