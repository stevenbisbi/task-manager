from datetime import datetime
from Task import Task 

def create_Task(taskList):
    while True:
        description = input("Ingrese la descripción de la tarea: ").strip()
        if not description:
            print("❌ La descripción no puede estar vacía")
            continue
        if len(description) > 200:
            print("❌ Máximo 200 caracteres")
            continue
        break

    # Crear tarea como instancia de la clase Task
    new_task = Task(
        task_id=len(taskList) + 1,
        description=description
    )
    taskList.append(new_task)

    # Generar mensaje de confirmación
    mensaje = "Tarea creada con éxito:"
    print( mensaje)