def markTaskAsCompleted(taskList, taskId):
    for task in taskList:
        if task.id == taskId:
            task.completed = True
            return task
    return "no se encuentra"