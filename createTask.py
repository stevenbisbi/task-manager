from datetime import datetime

def create_Task(taskList):
    """
    Maneja todo el proceso de creación de tareas
    Args:
        taskList: Lista existente de tareas
    Returns:
        tuple: (tarea_creada, mensaje_confirmación)
    """
    # Capturar descripción
    while True:
        description = input("Ingrese la descripción de la tarea: ").strip()
        if not description:
            print("❌ La descripción no puede estar vacía")
            continue
        if len(description) > 200:
            print("❌ Máximo 200 caracteres")
            continue
        break

    # Capturar prioridad con validación
    while True:
        priority = input("Prioridad (baja/media/alta): ").lower()
        if priority in ["", "baja", "media", "alta"]:
            priority = priority if priority else "media"
            break
        print("❌ Opción inválida. Use: baja, media o alta")

    # Crear tarea
    new_task = {
        'id': len(taskList) + 1,
        'description': description,
        'priority': priority,
        'completed': False,
        'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    taskList.append(new_task)

    # Generar mensaje de confirmación
    mensaje ="Tarea creada con éxito:"
    return  mensaje