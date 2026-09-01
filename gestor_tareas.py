import json
import os

ARCHIVO_TAREAS = "tareas.json"

def cargar_tareas():
    # Carga las tareas desde el archivo JSON si existe
    if not os.path.exists(ARCHIVO_TAREAS):
        return []
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def guardar_tareas(tareas):
    # Guarda la lista de tareas en el archivo JSON
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)

def agregar_tarea(titulo):
    tareas = cargar_tareas()
    nuevo_id = len(tareas) + 1 if tareas else 1
    nueva_tarea = {
        "id": nuevo_id,
        "titulo": titulo,
        "completada": False
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print(f"✅ Tarea agregada con éxito (ID: {nuevo_id})")

def listar_tareas():
    tareas = cargar_tareas()
    if not tareas:
        print("📭 No hay tareas registradas.")
        return
    print("\n--- 📋 TUS TAREAS ---")
    for t in tareas:
        estado = "[X]" if t["completada"] else "[ ]"
        print(f"{estado} {t['id']}. {t['titulo']}")
    print("----------------------\n")

def marcar_completada(id_tarea):
    tareas = cargar_tareas()
    encontrada = False
    for t in tareas:
        if t["id"] == id_tarea:
            t["completada"] = True
            encontrada = True
            break
    if encontrada:
        guardar_tareas(tareas)
        print(f"🎉 Tarea {id_tarea} marcada como completada.")
    else:
        print(f"⚠️ No se encontró la tarea con ID {id_tarea}.")

def eliminar_tarea(id_tarea):
    tareas = cargar_tareas()
    tareas_filtradas = [t for t in tareas if t["id"] != id_tarea]
    if len(tareas_filtradas) < len(tareas):
        guardar_tareas(tareas_filtradas)
        print(f"🗑️ Tarea {id_tarea} eliminada con éxito.")
    else:
        print(f"⚠️ No se encontró la tarea con ID {id_tarea}.")

def menu_principal():
    while True:
        print("\n=== 📌 GESTOR DE TAREAS ===")
        print("1. ➕ Agregar tarea")
        print("2. 📋 Listar tareas")
        print("3. ✅ Marcar tarea como completada")
        print("4. 🗑️ Eliminar tarea")
        print("5. 🚪 Salir")
        
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == "1":
            titulo = input("Escribe el nombre de la tarea: ")
            if titulo.strip():
                agregar_tarea(titulo)
            else:
                print("⚠️ El título no puede estar vacío.")
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            try:
                id_t = int(input("ID de la tarea a completar: "))
                marcar_completada(id_t)
            except ValueError:
                print("⚠️ Debes ingresar un número válido.")
        elif opcion == "4":
            try:
                id_t = int(input("ID de la tarea a eliminar: "))
                eliminar_tarea(id_t)
            except ValueError:
                print("⚠️ Debes ingresar un número válido.")
        elif opcion == "5":
            print("¡Hasta luego! 👋")
            break
        else:
            print("⚠️ Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()
