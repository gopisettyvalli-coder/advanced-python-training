import time
import asyncio

# Synchronous execution (blocks sequentially for each task)
def synchronous():
    for _ in range(3):
        time.sleep(1)


# Asynchronous execution (runs tasks concurrently during I/O waits)
async def asynchronous():
    async def fetch():
        await asyncio.sleep(1)

    await asyncio.gather(fetch(), fetch(), fetch())


# Synchronous time
start = time.perf_counter()
synchronous()
sync_time = time.perf_counter() - start


# Asynchronous time
start = time.perf_counter()
asyncio.run(asynchronous())
async_time = time.perf_counter() - start


print("Performance Comparison")
print("----------------------")
print("Synchronous:", round(sync_time, 2), "seconds")
print("Asynchronous:", round(async_time, 2), "seconds")

if async_time < sync_time:
    print("Asynchronous execution is faster.")
else:
    print("Synchronous execution is faster.")