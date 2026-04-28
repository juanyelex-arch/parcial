peliculas = ("rambo", "rocky", "soul")

precios = {
    "rambo": 39000,
    "rocky": 25000,
    "soul": 30000
}

compras = []

def comprar():
    try:
        pel = input("que pelicula quieres ver: ")

        if pel not in peliculas:
            print("no esta")
            return

        cant = int(input("cantidad: "))
        total = precios[pel] * cant

        compras.append((pel, cant, total))

        print("total:", total)

    except:
        print("error")

def ver():
    print(compras)


while True:
    op = input("\n1comprar 2salir: ")

    if op == "1":
        comprar()
    
    elif op == "2":
        break