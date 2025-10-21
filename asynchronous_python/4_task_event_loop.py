import asyncio


# Переменная log_events вшита в задачу, вставлять её не нужно
# log_events = [{"event": "Запрос на вход", "delay": 0.5},...{}]


async def fetch_log(item):
    event = item["event"]
    delay = item["delay"]
    await asyncio.sleep(delay)
    print(f"Событие: '{event}' обработано с задержкой {delay} сек.")


async def main():
    tasks = []
    for item in log_events:
        tasks.append(asyncio.create_task(fetch_log(item)))
    await asyncio.gather(*tasks)


asyncio.run(main())
