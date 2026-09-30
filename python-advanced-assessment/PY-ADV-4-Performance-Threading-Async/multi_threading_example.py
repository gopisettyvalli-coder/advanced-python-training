import threading

def worker(thread_name):
    print(thread_name, "started")
    print(thread_name, "completed")

thread1 = threading.Thread(target=worker, args=("Thread 1",))
thread2 = threading.Thread(target=worker, args=("Thread 2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads completed")