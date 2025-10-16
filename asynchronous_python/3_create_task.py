import asyncio


async def example_coroutine():
    await asyncio.sleep(1) 
    print("Hello from coroutine!")

async def main():
    task = asyncio.create_task(example_coroutine())  # создаем задачу из корутины example_coroutine()
    await task # ждем выполнения задачи

asyncio.run(main())
