import asyncio


async def search_keyword(news_list, keyword, delay=0):
    for news in news_list:
        if keyword.lower() in news.lower():
            await asyncio.sleep(delay)
            print(f"Найдено соответствие для '{keyword}': {news}")


async def main():
    tasks = [
        asyncio.create_task(search_keyword(news_list, "COVID-19")),
        asyncio.create_task(search_keyword(news_list, "игр")),
        asyncio.create_task(search_keyword(news_list, "новый вид"))
    ]
    await asyncio.gather(*tasks)


# Запуск программы
asyncio.run(main())
