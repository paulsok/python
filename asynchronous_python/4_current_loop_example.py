import asyncio


async def my_task():
    print("Running my task")


async def main():
    loop = asyncio.get_running_loop()
    print(type(loop))
    print(loop)
    loop.create_task(my_task())
    await asyncio.sleep(1)


asyncio.run(main())
