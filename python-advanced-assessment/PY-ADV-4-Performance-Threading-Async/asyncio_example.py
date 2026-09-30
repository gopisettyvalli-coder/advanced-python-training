import asyncio

async def cook(item, duration):
    print("Cooking", item)
    await asyncio.sleep(duration)
    print(item, "is ready!")

async def main():
    await asyncio.gather(
        cook("Eggs", 2),
        cook("Toast", 1)
    )

asyncio.run(main())