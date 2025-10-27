import asyncio


# Корутина для отправки запроса.
async def equipment_request(request):
    number = request.split(' ')[0]
    await asyncio.sleep(1)
    return f"{number} is Ok!"


# Корутина для управления отправкой запросов на заказ оборудования
async def send_requests():
    tasks = [asyncio.create_task(equipment_request(request)) for request in equipment_list]
    await asyncio.gather(*tasks)
    waiting_time = query_time()
    print(f"На отправку {len(tasks)} запросов потребовалось {waiting_time} секунд!")
