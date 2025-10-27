import asyncio


async def countdown(name, seconds):
    while seconds!=0:
        if name == "Квест на поиск сокровищ":
            print(f"{name}: Осталось {seconds} сек. Найди скрытые сокровища!")
            seconds -= 1
            await asyncio.sleep(1)
        else:
            print(f"{name}: Осталось {seconds} сек. Беги быстрее, дракон на хвосте!")
            seconds -= 1
            await asyncio.sleep(1)
    print(f"{name}: Задание выполнено! Что дальше?")


async def main():
    treasure_hunt = asyncio.create_task(countdown("Квест на поиск сокровищ", 10))
    dragon_escape = asyncio.create_task(countdown("Побег от дракона", 5))
    await asyncio.gather(treasure_hunt, dragon_escape)


asyncio.run(main())
