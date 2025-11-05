import asyncio
import random


async def task(num):
    await asyncio.sleep(delay := random.random())
    return f'Task {num} completed, {delay=:.3f}'


async def main():
    tasks = [asyncio.create_task(task(i)) for i in range(5)]

    for completed_task in asyncio.as_completed(tasks):
        # completed_task - объект корутины, создаваемый функцией as_completed(), возвращающий результат завершенной задачи.
        result = await completed_task
        print(result)


asyncio.run(main())
