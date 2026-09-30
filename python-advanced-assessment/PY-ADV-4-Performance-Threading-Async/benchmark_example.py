import time
import asyncio

def sync_download():
    time.sleep(1.5)
    time.sleep(1.5)

async def async_download():
    await asyncio.gather(
        asyncio.sleep(1.5),
        asyncio.sleep(1.5)
    )

start = time.perf_counter()
sync_download()
sync_time = time.perf_counter() - start

start = time.perf_counter()
asyncio.run(async_download())
async_time = time.perf_counter() - start

print("Synchronous time:", sync_time, "seconds")
print("Asynchronous time:", async_time, "seconds")