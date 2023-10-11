import os

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Agregar Producto")
    print("2 - Modificar datos")
    print("3 - Eliminar producto")
    print("4 - Ver stock")
    print("5 - Salir")


    #principal
while respuesta !="salir":
    menu()
    opt =input("\n Ingrese la opción que quiera realizar" )
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric(): 
        
        if int(opt)==1:
            from funciones import nuevo_producto
            nuevo_producto()
            print()
        elif int(opt)==2:
            from funciones import modificar_produc
            modificar_produc()
            print()
        elif int(opt)==3:
            from funciones import eliminar_produc
            eliminar_produc()
            print()
        elif int(opt)==4:
            from funciones import ver_stock
            ver_stock()
            print()
        elif int(opt)==5:
            respuesta="salir"
        else:
           print("Elija opción válida")
        
       
    else:
       print("Debe ingresar un número")
