import asyncio
import time


async def fetch_data(service_name, delay):
    print(f"Starting request to {service_name}...")
    await asyncio.sleep(delay)  # Simulates waiting for a network response
    print(f"Received response from {service_name}!")
    return {"service": service_name, "status": "Success"}


async def main():
    start_time = time.perf_counter()

    results = await asyncio.gather(
        fetch_data("User Service", 2),
        fetch_data("Payment Service", 3),
        fetch_data("Notification Service", 1),
    )

    end_time = time.perf_counter()

    print("\n--- Summary ---")
    for result in results:
        print("-", result)

    print(f"\nTotal execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())