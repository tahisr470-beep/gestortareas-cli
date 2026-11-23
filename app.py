
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


def mostrar_menu():
    print("\n===== SISTEMA DE GESTION DE TAREAS V1 =====")
    print("Seleccione una operacion:")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()

