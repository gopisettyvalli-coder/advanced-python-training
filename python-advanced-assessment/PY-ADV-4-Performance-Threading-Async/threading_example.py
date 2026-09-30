import threading

def process_task(task_name):
    print(f"Executing {task_name}")

thread1 = threading.Thread(
    target=process_task,
    args=("Task A",)
)

thread2 = threading.Thread(
    target=process_task,
    args=("Task B",)
)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All tasks completed")