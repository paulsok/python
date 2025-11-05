import asyncio


async def task_func(task_id):
    print(f"Задача {task_id} выполнена")
    return task_id


async def main():
    # Создаем несколько задач
    tasks = [asyncio.create_task(task_func(i), name=f'Task-{i}') for i in range(5)]

    # Ожидаем завершения всех задач
    _, pending = await asyncio.wait(tasks)

    # Проверяем, что все задачи завершены
    assert not pending, f"{len(pending)} ожидающих задач"
    for task in tasks:
        print(f"Результат задачи {task.get_name()}:", task.result())


asyncio.run(main())
