import asyncio


books_json = [
    {
        "Порядковый номер": 1,
        "Автор": "Rebecca Butler",
        "Название": "Three point south wear score organization.",
        "Год издания": "1985",
        "Наличие на полке": True
    },
    {
        "Порядковый номер": 2,
        "Автор": "Mark Cole",
        "Название": "Drive experience customer somebody pressure.",
        "Год издания": "1985",
        "Наличие на полке": False
    },
    ]


async def check_book(book):
    if not book["Наличие на полке"]:
        print(f'{book["Порядковый номер"]}: {book["Автор"]}: {book["Название"]} ({book["Год издания"]})')
        await asyncio.sleep(0.1)


async def main():
    tasks = [asyncio.create_task(check_book(book)) for book in books_json]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
