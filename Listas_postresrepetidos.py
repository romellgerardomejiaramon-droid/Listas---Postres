
import time


class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


class ListaIngredientes:
    def __init__(self):
        self.primero = None

    def buscar(self, nombre):
        actual = self.primero

        while actual is not None:
            if actual.nombre.strip().lower() == nombre.strip().lower():
                return True
            actual = actual.siguiente

        return False

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

    def eliminar(self, nombre):
        if self.primero is None:
            return False

        if self.primero.nombre.strip().lower() == nombre.strip().lower():
            self.primero = self.primero.siguiente
            return True

        actual = self.primero

        while actual.siguiente is not None:
            if actual.siguiente.nombre.strip().lower() == nombre.strip().lower():
                actual.siguiente = actual.siguiente.siguiente
                return True

            actual = actual.siguiente

        return False

    def mostrar(self):
        if self.primero is None:
            print("No hay ingredientes registrados.")
            return

        actual = self.primero
        numero = 1

        while actual is not None:
            print(str(numero) + ". " + actual.nombre)
            actual = actual.siguiente
            numero += 1


class Postre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = ListaIngredientes()


POSTRES = []


def buscar_postre(nombre):
    for postre in POSTRES:
        if postre.nombre.strip().lower() == nombre.strip().lower():
            return postre

    return None


def alta_postre(nombre):
    if nombre.strip() == "":
        print("El nombre del postre no puede estar vacio.")
        return None

    nuevo = Postre(nombre.strip())
    POSTRES.append(nuevo)
    POSTRES.sort(key=lambda postre: postre.nombre.lower())

    return nuevo


def baja_postre(nombre):
    postre = buscar_postre(nombre.strip())

    if postre is None:
        return False

    POSTRES.remove(postre)
    return True


def mostrar_postres():
    if len(POSTRES) == 0:
        print("No hay postres registrados.")
        return

    print("\nPostres ordenados alfabeticamente:")

    for postre in POSTRES:
        print("- " + postre.nombre)


def registrar_ingredientes(postre):
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


def mostrar_tiempo(inicio):
    tiempo = time.perf_counter() - inicio
    print(f"Tiempo de ejecucion: {tiempo:.6f} segundos")


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


def main():
    flan = Postre("Flan")
    flan.ingredientes.agregar("Huevo")
    flan.ingredientes.agregar("Leche")
    flan.ingredientes.agregar("Azucar")
    POSTRES.append(flan)

    gelatina = Postre("Gelatina")
    gelatina.ingredientes.agregar("Agua")
    gelatina.ingredientes.agregar("Grenetina")
    gelatina.ingredientes.agregar("Azucar")
    POSTRES.append(gelatina)

    pastel = Postre("Pastel")
    pastel.ingredientes.agregar("Harina")
    pastel.ingredientes.agregar("Huevo")
    pastel.ingredientes.agregar("Leche")
    POSTRES.append(pastel)

    POSTRES.sort(key=lambda postre: postre.nombre.lower())

    while True:
        print("\n========== MENU POSTRES ==========")
        print("1. Mostrar ingredientes de un postre")
        print("2. Agregar ingredientes")
        print("3. Eliminar un ingrediente")
        print("4. Dar de alta un postre")
        print("5. Dar de baja un postre")
        print("6. Mostrar todos los postres")
        print("7. Eliminar todos los elementos repetidos")
        print("8. Salir")

        opcion = input("Selecciona una opcion: ").strip()
        inicio_operacion = time.perf_counter()

        if opcion == "1":
            nombre = input("Nombre del postre: ").strip()
            postre = buscar_postre(nombre)

            if postre is None:
                print("El postre no existe.")
            else:
                print("\nIngredientes de " + postre.nombre + ":")
                postre.ingredientes.mostrar()

            mostrar_tiempo(inicio_operacion)

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

        elif opcion == "3":
            nombre = input("Nombre del postre: ").strip()
            postre = buscar_postre(nombre)

            if postre is None:
                print("El postre no existe.")
            else:
                ingrediente = input("Ingrediente a eliminar: ").strip()

                if ingrediente == "":
                    print("Debes escribir un ingrediente.")
                elif postre.ingredientes.eliminar(ingrediente):
                    print("Ingrediente eliminado correctamente.")
                else:
                    print("El ingrediente no existe.")

            mostrar_tiempo(inicio_operacion)

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

        elif opcion == "5":
            nombre = input("Nombre del postre a eliminar: ").strip()

            if baja_postre(nombre):
                print("Postre eliminado junto con sus ingredientes.")
            else:
                print("El postre no existe.")

            mostrar_tiempo(inicio_operacion)

        elif opcion == "6":
            mostrar_postres()
            mostrar_tiempo(inicio_operacion)

        elif opcion == "7":
            menu_opcion_7()
            mostrar_tiempo(inicio_operacion)

        elif opcion == "8":
            print("\nPrograma terminado.")
            mostrar_tiempo(inicio_operacion)
            break

        else:
            print("Opcion invalida.")
            mostrar_tiempo(inicio_operacion)


if __name__ == "__main__":
    main()
