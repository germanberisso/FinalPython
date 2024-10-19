class Producto: 
    def __init__(self,nombre,cantidad):
        self.nombre=nombre
        self.cantidad=cantidad

productos=[]

def mostrar_lista():
    j=0
    while j<len(productos):
        print(productos[j].nombre,"",productos[j].cantidad)
        j+=1

# Menú de opciones
i=0
while (i==0):
    print("***Menú de Gestión de Productos\n")
    print("1. Agregar productos nuevos")
    print("2. Consulta de productos registrados")
    print("3. Salir")

# Solicitar al usuario que seleccione una opción
    opcion = int(input("Por favor, selecciona una opción (1-3): "))

    if opcion==1:
        print("Agregar producto")
        nom=input("Ingrese el nombre del producto: ")
        cant=input("Ingrese la cantidad del producto: ")
        prod=Producto(nom,cant)
        productos.append(prod)
        print("Producto agregado")
    elif opcion==2:
        print("***Listado de productos***")
        mostrar_lista()
    elif opcion==3:
        exit()
    else:
        print("opcion invalida")
        