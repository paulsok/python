import asyncio


async def activate_portal(x):
    print(f"Активация портала в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 2


async def perform_teleportation(x):
    print(f"Телепортация в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x + 2


async def recharge_portal(x):
    print(f"Подзарядка портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 3


async def check_portal_stability(x):
    print(f"Проверка стабильности портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x + 4


async def restore_portal(x):
    print(f"Восстановление портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 5


async def close_portal(x):
    print(f"Закрытие портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x - 1


async def portal_operator():
    activation_result = await activate_portal(2)

    teleportation_task = asyncio.create_task(perform_teleportation(3))
    recharge_task = asyncio.create_task(recharge_portal(4))
    check_task = asyncio.create_task(check_portal_stability(5))
    restore_task = asyncio.create_task(restore_portal(6))
    close_task = asyncio.create_task(close_portal(7))

    results = await asyncio.gather(
        teleportation_task,
        recharge_task,
        check_task,
        restore_task,
        close_task
    )

    teleportation_result, recharge_result, check_result, restore_result, close_result = results

    print(f"Результат активации портала: {activation_result} единиц энергии")
    print(f"Результат телепортации: {teleportation_result} единиц времени")
    print(f"Результат подзарядки портала: {recharge_result} единиц энергии")
    print(f"Результат проверки стабильности: {check_result} единиц времени")
    print(f"Результат восстановления портала: {restore_result} единиц энергии")
    print(f"Результат закрытия портала: {close_result} единиц времени")


if __name__ == "__main__":
    asyncio.run(portal_operator())
