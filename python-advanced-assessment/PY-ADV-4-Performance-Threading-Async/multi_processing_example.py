import multiprocessing

def worker(process_name):
    print(process_name, "started")
    print(process_name, "completed")

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=worker, args=("Process 1",))
    process2 = multiprocessing.Process(target=worker, args=("Process 2",))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Both processes completed")