import time
from out import fast

def fib(n): return n if n < 2 else fib(n-1) + fib(n-2)

t = time.perf_counter(); fib(35);      print("python", time.perf_counter() - t)
t = time.perf_counter(); fast.Fib(35); print("go    ", time.perf_counter() - t)