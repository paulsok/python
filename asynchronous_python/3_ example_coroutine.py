import asyncio
import time


async def example_coroutine(n):
    print(f"Hello from coroutine #{n}! {time.perf_counter() - start:.3f} секунды")
    await asyncio.sleep(1)
    print(f"Coroutine #{n} completed! {time.perf_counter() - start:.3f} секунды")


async def main():
    for num in range(1, 11):
        await example_coroutine(num)


start = time.perf_counter()
asyncio.run(main())
print(f"Программа выполнена за {time.perf_counter() - start:.3f} секунды")
