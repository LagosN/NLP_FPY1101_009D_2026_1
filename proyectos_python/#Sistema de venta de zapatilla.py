#Sistema de venta de zapatilla 

#Diccionario con stock zaptillas

inventario = {
    "001" : {"modelo" : "Air Max", "precio" : 89990, "stock" : 15},
    "002" : {"modelo" : "Classic", "precio" : 49990, "stock" : 15},
    "003" : {"modelo" : "Runner", "precio" : 69990, "stock" : 15},
    "004" : {"modelo" : "basquet", "precio" : 79990, "stock" : 15},
}

#Metodos DEF


def mostrar_invetario():
    print("="*60)
    print("Inventario tienda")
    print("="*60)

    for codigo , dato in inventario.items():
        print(f"{codigo}  | {dato ["modelo"]} | ${dato["precio"]} | {dato["stock"]}")
    

#Validar el ingreso el codigo de la zapatilla a vender
def procesar_venta():
    mostrar_invetario()
    codigo_zapatilla = input("Ingreasa el codigo de la zaptilla a vender:")
    if codigo_zapatilla not in inventario:
        print("La zapatilla no esta registrada en el inventario")
        return
    
    try:
        cantidad = int(input("Ingrese la cantidad de zapatillas a vender"))
    except ValueError as e:
        print(f"Error, debe ingresar un codio de zapatilla valido")
        return
    
    if cantidad <= 0:
        print("Error: la cantidad no puede ser menor a cero.")
    elif cantidad > inventario[codigo_zapatilla]["stock"]:
        print("Error no existe suficiente stock.")
        return
    
    #Calcular venta


    precio_unitario = inventario[codigo_zapatilla]["precio"]

    total_venta = precio_unitario * cantidad

    #Descontar de stock

    #inventario[codigo_zapatilla]["stock"] = inventario[codigo_zapatilla]["stock"] - cantidad
    inventario[codigo_zapatilla]["stock"]-= cantidad

    #Generar boleta de venta 

    print("\n =" *60)

    print("BOLETA ELECTRONICA")

    print(" =" *60)

    print(f"producto:{inventario[codigo_zapatilla]["modelo"]}")
    print(f"Precio unitario: {inventario[codigo_zapatilla]["modelo"]}")
    print(f"Cantidad: {cantidad}")
    print(f"Total a pagar: ${total_venta}")
    print("-"*60)



#metodo def

def main():
    print("="*60)
    print("Bienvenido al sistema de ventas")
    print("="*60)
    while True:
        print("Opciones del sistema: ")
        print("[1] Ver inventario")
        print("[2] Realizar venta")
        print("[3] Salir")
        opc = int(input("Ingresa una de las opciones:"))
        if opc == 1:
            mostrar_invetario()
        elif opc == 2:
            procesar_venta()
        elif opc == 3:
            print("Muchas gracias por comprar")
            exit(0)
        else:
            print("Opcion ingresada no es valida.")


main()
        

