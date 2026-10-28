
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
            if actual.nombre.lower() == nombre.lower():
                return True
            actual = actual.siguiente

        return False

    def agregar(self, nombre):
        if self.buscar(nombre):
            return False

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

        if self.primero.nombre.lower() == nombre.lower():
            self.primero = self.primero.siguiente
            return True

        actual = self.primero

        while actual.siguiente is not None:
            if actual.siguiente.nombre.lower() == nombre.lower():
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
        if postre.nombre.lower() == nombre.lower():
            return postre

    return None


def alta_postre(nombre):
    if nombre == "":
        print("El nombre del postre no puede estar vacio.")
        return None

    if buscar_postre(nombre) is not None:
        print("El postre ya existe.")
        return None

    nuevo = Postre(nombre)
    POSTRES.append(nuevo)
    POSTRES.sort(key=lambda postre: postre.nombre.lower())

    return nuevo


def baja_postre(nombre):
    postre = buscar_postre(nombre)

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
    print("Escribe FIN o LISTO para terminar.")

    while True:
        ingrediente = input("Nuevo ingrediente: ").strip()

        if ingrediente.upper() in ("FIN", "LISTO"):
            print("Registro de ingredientes terminado.")
            break

        if ingrediente == "":
            print("El ingrediente no puede estar vacio.")
        elif postre.ingredientes.agregar(ingrediente):
            print("Ingrediente agregado correctamente.")
        else:
            print("El ingrediente ya existe.")


def mostrar_tiempo(inicio_operacion):
    tiempo = time.perf_counter() - inicio_operacion
    print(f"Tiempo de ejecucion de la opcion: {tiempo:.6f} segundos")


def main():
    flan = alta_postre("Flan")
    flan.ingredientes.agregar("Huevo")
    flan.ingredientes.agregar("Leche")
    flan.ingredientes.agregar("Azucar")

    gelatina = alta_postre("Gelatina")
    gelatina.ingredientes.agregar("Agua")
    gelatina.ingredientes.agregar("Grenetina")
    gelatina.ingredientes.agregar("Azucar")

    pastel = alta_postre("Pastel")
    pastel.ingredientes.agregar("Harina")
    pastel.ingredientes.agregar("Huevo")
    pastel.ingredientes.agregar("Leche")

    while True:
        print("\n========== MENU POSTRES ==========")
        print("1. Mostrar ingredientes de un postre")
        print("2. Agregar ingredientes")
        print("3. Eliminar un ingrediente")
        print("4. Dar de alta un postre")
        print("5. Dar de baja un postre")
        print("6. Mostrar todos los postres")
        print("7. Salir")

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
                registrar_ingredientes(postre)

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
            elif buscar_postre(nombre) is not None:
                print("El postre ya existe.")
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
            print("\nPrograma terminado.")
            mostrar_tiempo(inicio_operacion)
            break

        else:
            print("Opcion invalida.")
            mostrar_tiempo(inicio_operacion)


if __name__ == "__main__":
    main()
