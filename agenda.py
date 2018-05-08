agenda = {}

def agregar_contacto():
    """Funcion para agregar contacto"""
    nombre = input('Nombre del nuevo contacto:')
    numero = input('Ingresa el número')
    agenda[nombre] = numero
    print('Contacto %s agregado' % nombre)
    

def remover_contacto():
    """Funcion para eliminar contacto"""
    

def actualizar_contacto():
    """Funcion para actualizar contacto"""
    


def ver_contacto():
    """Funcion para ver contacto"""
    print('*' * 8 + 'Contacto' + '*' * 8)
    nombre = input('Nombre de contacto: ')
    try:
        print('%s: %s' %(nombre, agenda[nombre]))
    except KeyError:
        'Ese contacto no existe'
    print('*' * 23)
    


def ver_todos():
    """Funcion para ver todos los contactos"""
    


print('Bienvenido a la agenda')
while True:
    print('1 - Agregar contacto')
    print('2 - Remover contacto')
    print('3 - Actualizar contacto')
    print('4 - Ver un contacto')
    print('5 - Ver todos los contactos')
    print('6 - Salir')
    try:
        op = int(input('Seleccione operacion: '))
    except ValueError:
        print('Ingrese un numero')
    else:
        if op == 1:
            agregar_contacto()
        elif op == 2:
            remover_contacto()
        elif op == 3:
            actualizar_contacto()
        elif op == 4:
            ver_contacto()
        elif op == 5:
            ver_todos()
        else:
            break
