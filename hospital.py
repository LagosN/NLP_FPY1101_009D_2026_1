



#Nombre  = str / Edad = int / Temperatura = float / Estado = bool
pacientes = [{"nombre": "Juan", "edad": 20 , "temperatura": 36.3, "estado": False}

]


print("="*60)
print("Menu registro de paciente")
print("="*60)
print("[1] Agregar paciente.")
print("[2] Buscar paciente.")
print("[3] Eliminar paciente.")
print("[4] Actualizar estado.")
print("[5] Mostar pacientes. ")
print("[6] Salir. ") 



def agregar_paciente():
    
    while True:
        nombre_p = input("Ingrese el nombre del paciente:")
        if nombre_p == "":
            print("El nombre no puede quedar vacio.")
            continue
        elif nombre_p.strip() == "":
            print("El nombre no puede tener solo espacios.")
            continue
        else:
            print("Nombre agregado")
            break
    while True:
        edad_p = int(input("Ingrese la edad del paciente:"))
        if edad_p <= 0:
            print("El numero no puede ser menor a 0.")
            continue
        else:
            print("Edad agregada.")
            break
    while True:
        temperatura_p = float(input("Ingrese la temperatura del paciente, ejemplo de usa coma: 36.0:"))
        if temperatura_p < 35 or temperatura_p > 42:
            print("El numero debes estar entre 35 y 42")
            continue
        else:
            print("Temperatura agregada")
            break
    hospital = {'nombre':nombre_p, 'edad':edad_p, 'temperatura':temperatura_p, 'estado': False 
    }
    pacientes.append(hospital)
    print(pacientes)

def buscador_paciente(lista, nombre_paciente):
    for i in range(len(lista)):
        if lista[i]['nombre'] == nombre_paciente:
            return i
        
    return -1

def buscar_paciente_lista():
    while True:
        nombre_p = str(input("Ingrese el nombre del paciente:"))
        if nombre_p == "":
            print("El nombre no puede quedar vacio.")
            continue
        elif nombre_p.strip() == "":
            print("El nombre no puede tener solo espacios.")
            continue
        else:
            break
    posicion = buscador_paciente(pacientes, nombre_p)
    if posicion != -1:
        paciente_encontrado = pacientes[posicion]
        print(f"¡Paciente encontrado en la posición {posicion }!")
        print(paciente_encontrado)
    else:
        print(f" El paciente '{nombre_p}' no se encuentra registrado en el sistema.")

def eliminar_paciente():
    while True:
        nombre_p = input("Ingrese el nombre del paciente:")
        if nombre_p == "":
            print("El nombre no puede quedar vacio.")
            continue
        elif nombre_p.strip() == "":
            print("El nombre no puede tener solo espacios.")
            continue
        else:
            break
    posicion = buscador_paciente(pacientes, nombre_p)
    if posicion != -1:
        eliminado = pacientes.pop(posicion)
        print("Paciente eliminado:", eliminado["nombre"])
        
    else:
        print(f" El paciente '{nombre_p}' no se encuentra registrado en el sistema.")


def actualizar_estado(lista):
    for e in lista:
        if e['temperatura'] <= 37.0:
            e["estado"] = True
            print("Estado de pacientes actualizdo.")
        else:
            e['estado'] = False


def mostrar_paciente():
    print(f"Nombre {pacientes['nombre']} ''  ")
    print(f"Edad: {pacientes['edad']}")
    print(f"Temperatura: {pacientes['temperatura']}")
    print(f"\n Estado: {pacientes['estado']}")

def menu():
    while True:
        opc = int(input("Ingrese una de las opciones"))
        if opc == 1:
            agregar_paciente(pacientes)
        elif opc == 2:
            buscar_paciente_lista()
        elif opc == 3:
            eliminar_paciente()    
        elif opc == 4:
            actualizar_estado(pacientes)
        elif opc == 5:
            actualizar_estado(pacientes)
            mostrar_paciente()
        elif opc == 6:
            print("Gracias por usar el programa")
            break   
        
menu()