import asyncio


async def study_course(name, course, steps, speed):
    print(f"{name} начал проходить курс {course}.")
    reading_time = round(steps / speed, 2)
    await asyncio.sleep(reading_time)
    print(f"{name} прошел курс {course} за {reading_time} ч.")



async def main():
    tasks = []
    for name, details in students.items():
        task = asyncio.create_task(study_course(name, **details))
        tasks.append(task)

    await asyncio.gather(*tasks)


asyncio.run(main())
