# Listas Postres

El programa utiliza la clase NodoIngrediente para almacenar el nombre de cada ingrediente y la referencia al siguiente nodo. La clase ListaIngredientes administra los ingredientes mediante los métodos buscar(), agregar(), eliminar() y mostrar(), que permiten buscar, agregar, eliminar y visualizar ingredientes. La clase Postre almacena el nombre del postre y su lista de ingredientes. La variable POSTRES contiene todos los postres ordenados alfabéticamente. Las funciones buscar_postre(), alta_postre(), baja_postre() y mostrar_postres() permiten buscar, registrar, eliminar y mostrar postres. La función registrar_ingredientes() permite agregar varios ingredientes hasta escribir FIN o LISTO, mientras que mostrar_tiempo() calcula el tiempo de ejecución de cada opción. En el menú de la terminal, la opción 1 muestra los ingredientes de un postre, la opción 2 permite agregar varios ingredientes, la opción 3 elimina un ingrediente, la opción 4 registra un postre nuevo con sus ingredientes, la opción 5 elimina un postre, la opción 6 muestra todos los postres y la opción 7 termina el programa. Si se introduce una opción inválida o un dato inexistente, se muestra un mensaje y el programa continúa funcionando hasta que se selecciona la opción de salida.

# Listas Postres repetidos 

El programa administra una lista de postres ordenados alfabéticamente y sus ingredientes mediante listas enlazadas, donde cada ingrediente se guarda en un nodo que contiene su nombre y un enlace al siguiente nodo. Al ejecutarlo en la terminal, aparecen ocho opciones: la opción 1 muestra los ingredientes de un postre, la opción 2 permite agregar ingredientes aunque ya existan, la opción 3 elimina la primera aparición del ingrediente indicado, la opción 4 registra nuevos postres aunque tengan el mismo nombre que otro, la opción 5 elimina un postre y sus ingredientes, la opción 6 muestra todos los postres registrados, la opción 7 abre un submenú para consultar los postres e ingredientes repetidos, eliminarlos por separado o eliminar todos los duplicados, y la opción 8 termina el programa. Internamente, las funciones buscan los postres y recorren los nodos de las listas enlazadas para mostrar, agregar o eliminar elementos; la opción 7 utiliza conjuntos para identificar nombres repetidos y conserva la primera aparición de cada ingrediente o postre, eliminando las siguientes. Además, el programa utiliza la función perf_counter() del módulo time para medir y mostrar en la terminal el tiempo de ejecución de las opciones.

# Nuevo en el código 

def agregar(self, nombre):
    nuevo = NodoIngrediente(nombre)

    if self.primero is None:
        self.primero = nuevo
    else:
        actual = self.primero

        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevo

    return True


def buscar_postres_repetidos():
    vistos = set()
    repetidos = []

    for postre in POSTRES:
        nombre = postre.nombre.strip().lower()

        if nombre in vistos:
            repetidos.append(postre)
        else:
            vistos.add(nombre)

    return repetidos


def buscar_ingredientes_repetidos():
    repetidos = []

    for postre in POSTRES:
        vistos = set()
        actual = postre.ingredientes.primero

        while actual is not None:
            nombre = actual.nombre.strip().lower()

            if nombre in vistos:
                repetidos.append((postre.nombre, actual.nombre))
            else:
                vistos.add(nombre)

            actual = actual.siguiente

    return repetidos


def limpiar_postres_repetidos():
    vistos = set()
    conservados = []
    eliminados = []

    for postre in POSTRES:
        nombre = postre.nombre.strip().lower()

        if nombre in vistos:
            eliminados.append(postre.nombre)
        else:
            vistos.add(nombre)
            conservados.append(postre)

    POSTRES[:] = conservados
    POSTRES.sort(key=lambda postre: postre.nombre.lower())

    print("\nPostres repetidos eliminados:")

    if eliminados:
        for nombre in eliminados:
            print("- " + nombre)
    else:
        print("No se encontraron postres repetidos.")

    print("Cantidad de postres eliminados:", len(eliminados))


def limpiar_ingredientes_repetidos():
    total = 0

    for postre in POSTRES:
        vistos = set()
        actual = postre.ingredientes.primero
        anterior = None

        while actual is not None:
            nombre = actual.nombre.strip().lower()

            if nombre in vistos:
                print(
                    "Eliminado: " + actual.nombre
                    + " del postre " + postre.nombre
                )
                anterior.siguiente = actual.siguiente
                total += 1
            else:
                vistos.add(nombre)
                anterior = actual

            actual = actual.siguiente

    if total == 0:
        print("No se encontraron ingredientes repetidos.")

    print("Cantidad de ingredientes eliminados:", total)


def menu_opcion_7():
    while True:
        print("\n====== LIMPIEZA DE ELEMENTOS REPETIDOS ======")
        print("1. Mostrar postres repetidos")
        print("2. Mostrar ingredientes repetidos")
        print("3. Eliminar postres repetidos")
        print("4. Eliminar ingredientes repetidos")
        print("5. Eliminar todos los repetidos")
        print("6. Regresar al menu principal")

        opcion = input("Selecciona una opcion: ").strip()
        inicio = time.perf_counter()

        if opcion == "1":
            repetidos = buscar_postres_repetidos()

            if repetidos:
                print("\nPostres repetidos encontrados:")

                for postre in repetidos:
                    print("- " + postre.nombre)

                print("Cantidad de postres repetidos:", len(repetidos))
            else:
                print("No se encontraron postres repetidos.")

        elif opcion == "2":
            repetidos = buscar_ingredientes_repetidos()

            if repetidos:
                print("\nIngredientes repetidos encontrados:")

                for nombre_postre, ingrediente in repetidos:
                    print("- " + ingrediente + " en " + nombre_postre)

                print("Cantidad de ingredientes repetidos:", len(repetidos))
            else:
                print("No se encontraron ingredientes repetidos.")

        elif opcion == "3":
            limpiar_postres_repetidos()

        elif opcion == "4":
            limpiar_ingredientes_repetidos()

        elif opcion == "5":
            print("\n--- Eliminando postres repetidos ---")
            limpiar_postres_repetidos()

            print("\n--- Eliminando ingredientes repetidos ---")
            limpiar_ingredientes_repetidos()

        elif opcion == "6":
            mostrar_tiempo(inicio)
            break

        else:
            print("Opcion invalida.")

        mostrar_tiempo(inicio)


# Fragmento modificado de la opcion 2:
elif opcion == "2":
    nombre = input("Nombre del postre: ").strip()
    postre = buscar_postre(nombre)

    if postre is None:
        print("El postre no existe.")
    else:
        print("\nAgregando ingredientes a " + postre.nombre)
        print("Escribe FIN para terminar.")

        while True:
            ingrediente = input("Nuevo ingrediente: ").strip()

            if ingrediente.upper() == "FIN":
                print("Registro de ingredientes terminado.")
                break

            if ingrediente == "":
                print("El ingrediente no puede estar vacio.")
            else:
                postre.ingredientes.agregar(ingrediente)
                print("Ingrediente agregado correctamente.")

    mostrar_tiempo(inicio_operacion)


# Fragmento modificado de la opcion 4:
elif opcion == "4":
    nombre = input("Nombre del nuevo postre: ").strip()

    if nombre == "":
        print("El nombre del postre no puede estar vacio.")
    else:
        nuevo = Postre(nombre)
        registrar_ingredientes(nuevo)

        if nuevo.ingredientes.primero is not None:
            POSTRES.append(nuevo)
            POSTRES.sort(key=lambda postre: postre.nombre.lower())
            print("Postre registrado correctamente.")
        else:
            print("El postre no fue registrado porque no tiene ingredientes.")

    mostrar_tiempo(inicio_operacion)


# Fragmento modificado de la opcion 7:
elif opcion == "7":
    menu_opcion_7()
    mostrar_tiempo(inicio_operacion)
