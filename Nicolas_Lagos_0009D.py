#biblioteca
biblioteca = [
    {'titulo': 'La Catedral', 'copias': 2, 'prestamo':10, 'disponible': False}
             ]




print("Menu Principal")
print("[1] Agregar libro")
print("[2] Buscar libro")
print("[3] Eliminar libro")
print("[4] Actualizar disponibilidad")
print("[5] Mostrar libros")
print("[6] Salir")



def agregar_libro():
    nombre_nuevo = input("Ingresa el nombre del libro:")
    if nombre_nuevo.strip() == "":
        print("No puedes usar solo espacios.")
        return
    elif nombre_nuevo == "": 
        print("No puedes dejar vacio el nombre.")
        return 
    print("Libro agregado")
    try:
        copias_nueva = int(input("Ingresa la cantidad de copias disponibles"))
        if copias_nueva <= 0:
            print("Debes agregar un numero mayor a 0")
    except ValueError as e:
        print("Error solo puedes agregar numeros")
    print("Cantidad agregada")

    try:
        periodo_prestamo = int(input("Ingresa la cantidad de dias que usaras el libro"))
        if copias_nueva <= 0:
            print("Debes agregar un numero mayor a 0")
    except ValueError as e:
        print("Error solo puedes agregar numeros")
    print("Cantidad de dias agregado")
    #biblioteca.append([nombre_nuevo])
    biblioteca = { 'titulo': nombre_nuevo, 'copias': copias_nueva, 'prestamo': periodo_prestamo, 'diponible': 'False'}
    return biblioteca
    
def posicion_libro(lista, nombre_buscar):
    for i in range(len(lista)):
        if lista[i]['titulo'] == nombre_buscar:
            return i
    return -1

def buscar_libro():
    libro_biblioteca = input("Ingresa el nombre del libro:")
    if libro_biblioteca.strip() == "":
        print("No puedes usar solo espacios.")
        return
    elif libro_biblioteca == "": 
        print("No puedes dejar vacio el nombre.")
        return 
    posicion = posicion_libro(biblioteca, libro_biblioteca)

    print(f"Libro en {posicion}")
    return posicion

def eliminar_libro():
    libro_biblioteca = input("Ingresa el nombre del libro:")
    if libro_biblioteca.strip() == "":
        print("No puedes usar solo espacios.")
        return
    elif libro_biblioteca == "": 
        print("No puedes dejar vacio el nombre.")
        return 
    posicion = posicion_libro(biblioteca, libro_biblioteca)

    if posicion != -1:
        eliminar = biblioteca.pop[posicion]
        print(f"Se elimino el libro {libro_biblioteca}")
    else:
        print("Libro no encontrado")
        return
    
def actualizar_disponibilidad():
    for e in biblioteca:
        if e['copias'] >= 1:
            e['disponible'] = True
        else:
            e['disponible'] =False

def mostrar_libros():
    actualizar_disponibilidad()
    
    print(f"Nombre: {biblioteca:'titulo'}")
    print(f"Copias: {biblioteca:'copias'}")
    print(f"Prestamo: {biblioteca:'prestamo'}")
    print(f"Estado: {biblioteca:'estado'}")
def menu():
    while True:
        try:
            opc = int(input("Ingrese una de las opciones"))
            if opc <= 0:
                print("Debes escribir un numero del 1 a 6")
        except ValueError:
            print("Solo puedes agregar un numero")
        if opc == 1:
            agregar_libro()
        elif opc == 2:
            buscar_libro()
        elif opc == 3:
            eliminar_libro()
        elif opc == 4:
            actualizar_disponibilidad()
        elif opc == 5:
            mostrar_libros()
        elif opc == 6:
            print("Gracias por usar la app")
            break

menu()
