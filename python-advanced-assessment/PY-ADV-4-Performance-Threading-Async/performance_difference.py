import time
import threading

def sequential():
    time.sleep(2)
    time.sleep(3)

def multithreaded():
    t1 = threading.Thread(target=time.sleep, args=(2,))
    t2 = threading.Thread(target=time.sleep, args=(2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

start = time.perf_counter()
sequential()
seq_time = time.perf_counter() - start

start = time.perf_counter()
multithreaded()
thread_time = time.perf_counter() - start


print("Performance Comparison")
print("----------------------")
print("Sequential:", round(seq_time, 2), "seconds")
print("Multithreaded:", round(thread_time, 2), "seconds")

if thread_time < seq_time:
    print("Multithreaded execution is faster.")
else:
    print("Sequential execution is faster.")