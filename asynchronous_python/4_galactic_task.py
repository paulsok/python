import asyncio


async def activate_portal(x):
    print(f"Активация портала в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 2


async def perform_teleportation(x):
    print(f"Телепортация в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x + 2


async def portal_operator():
    task1 = asyncio.ensure_future(activate_portal(2))
    result = await asyncio.gather(task1)
    if result[0] > 4:
        task2 = asyncio.ensure_future(perform_teleportation(1))
    else:
        task2 = asyncio.ensure_future(perform_teleportation(result[0]))
    result2 = await asyncio.gather(task2)
    print(f"Результат активации портала: {result[0]} единиц энергии")
    print(f"Результат телепортации: {result2[0]} единиц времени")


if __name__ == '__main__':
    asyncio.run(portal_operator())
