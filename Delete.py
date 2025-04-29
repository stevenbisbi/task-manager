from Task import Task

def deleteTask(taskList, taskId):
    for index in range(len(taskList)):
        if taskList[index].id == taskId:
            del taskList[index]
            return "Task deleted"
    return "Tarea no encontrada"