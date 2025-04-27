def listAllTasks(taskList):
    for task in taskList:
        print(f"{task.id} - {task.description} - Completed: {task.completed}")
