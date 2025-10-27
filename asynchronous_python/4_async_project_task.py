import asyncio


# Словарь tasks_dependencies = {} вшит в задачу, вставлять его в решение не нужно.
async def execute_subtask(subtask):
    name = subtask["название"]
    duration = subtask["время"]
    if duration > 5:
        await asyncio.sleep(5)
        print(f"Подзадача: {name} не успела выполниться в срок, за {duration} сек.")
        return False
    else:
        await asyncio.sleep(duration)
        print(f"Подзадача: {name} успела выполниться в срок, за {duration} сек.")
        return True


async def execute_task(task_name, task_info):
    stages = task_info["этапы"]
    results = await asyncio.gather(*(execute_subtask(s) for s in stages))
    if all(results):
        print(f"Задача: {task_name} = все подзадачи выполнены.")
    else:
        print(f"Задача: {task_name} не выполнилась в срок, т.к. одна или несколько подзадач заняли слишком много времени.")


async def main():
    for name, info in tasks_dependencies.items():
        await execute_task(name, info)


asyncio.run(main())
