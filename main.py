from checkwork import markTaskAsCompleted
from Delete import deleteTask
from taskList import listAllTasks
from createTask import create_Task
def main():
    taskList = []
    while True:
        print("\n=== Task Manager ===")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":            
            create_Task(taskList)
                   
        elif choice == "2":
            listAllTasks(taskList)
        
        elif choice == "3":
            task_id = int(input("Ingrese el ID de la tarea a marcar como completada: "))
            result = markTaskAsCompleted(taskList, task_id)
            if result == "Task not found":
                print(result)
            else:
                print(f"Tarea {task_id} marcada como completada.")
        
        elif choice == "4":
            task_id = int(input("Ingrese el ID de la tarea a eliminar: "))
            result = deleteTask(taskList, task_id)
            print(result)
        
        elif choice == "5":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()