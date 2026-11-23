
tareas = []


def agregar_tarea():
    titulo = input("Ingrese el nombre de la tarea: ")
    tareas.append({
        "titulo": titulo,
        "completada": False
    })
    print("Tarea agregada correctamente.")


def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return

    print("\n===== LISTA DE TAREAS =====")

    for i, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['titulo']} - {estado}")


def completar_tarea():
    listar_tareas()

    if not tareas:
        return

    try:
        numero = int(input("Numero de tarea a completar: "))

        if 1 <= numero <= len(tareas):
            tareas[numero - 1]["completada"] = True
            print("Tarea completada correctamente.")
        else:
            print("Numero invalido.")
    except ValueError:
        print("Ingrese un numero valido.")


def eliminar_tarea():
    listar_tareas()

    if not tareas:
        return

    try:
        numero = int(input("Numero de tarea a eliminar: "))

        if 1 <= numero <= len(tareas):
            tareas.pop(numero - 1)
            print("Tarea eliminada correctamente.")
        else:
            print("Numero invalido.")
    except ValueError:
        print("Ingrese un numero valido.")


def mostrar_menu():
    print("\n===== SISTEMA DE GESTION DE TAREAS V1 =====")
    print("Seleccione una operacion:")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()
