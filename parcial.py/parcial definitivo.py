peliculas = {
    "rambo": {
        "precio": 39000,
        "horarios": ["3pm", "7pm", ":9pm"]
    },
    "rocky": {
        "precio": 25000,
        "horarios": ["2pm", "5pm", "8pm"]
    },
    "soul": {
        "precio": 30000,
        "horarios": ["10am", "11am", "11am"]
    }
}

compras = []


def mostrar_peliculas():
    print("\ncartelera:")
    for nombre, datos in peliculas.items():
        print(f"\n{nombre}")
        print(f"precio: ${datos['precio']}")
        print("horarios:", ", ".join(datos["horarios"]))


def comprar():
    mostrar_peliculas()

    pel = input("\nque pelicula quieres: ").strip().lower()
    if pel not in peliculas:
        print("pelicula no disponible")
        return

    print("horarios disponibles:", ", ".join(peliculas[pel]["horarios"]))
    hora = input("elige un horario: ").strip()

    if hora not in peliculas[pel]["horarios"]:
        print("horario no valido")
        return

    try:
        cant = int(input("cantidad de boletas: "))
        if cant <= 0:
            print("cantidad invalida")
            return
    except ValueError:
        print("debes ingresar un numero")
        return

    precio = peliculas[pel]["precio"]
    total = precio * cant

    compras.append({
        "pelicula": pel,
        "horario": hora,
        "cantidad": cant,
        "total": total
    })

    print(f"total a pagar: ${total}")


def ver_compras():
    if not compras:
        print("\nno hay compras")
        return

    total_general = 0
    print("\ncompras realizadas:")

    for c in compras:
        print(f"{c['pelicula']} | {c['horario']} | cant: {c['cantidad']} | total: ${c['total']}")
        total_general += c["total"]

    print(f"\ntotal general: ${total_general}")


def menu():
    while True:
        print("\nmenu")
        print("1. ver cartelera")
        print("2. comprar")
        print("3. ver compras")
        print("4. salir")

        op = input("opcion: ").strip()

        if op == "1":
            mostrar_peliculas()
        elif op == "2":
            comprar()
        elif op == "3":
            ver_compras()
        elif op == "4":
            break
        else:
            print("opcion invalida")


menu()