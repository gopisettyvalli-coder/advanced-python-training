import threading

def process_data():
    print("Processing...")

    result = 0
    for i in range(1000000):
        result += i * 2

    print("Data processed")

thread1 = threading.Thread(target=process_data)
thread2 = threading.Thread(target=process_data)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads completed")