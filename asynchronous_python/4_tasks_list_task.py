import asyncio


async def main():
    awaitables = [aw for aw in await get_coros_and_tasks()]
    tasks = [asyncio.ensure_future(x) for x in awaitables]
    result = await asyncio.gather(*tasks)
    return result
