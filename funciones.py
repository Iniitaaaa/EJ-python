productos={}

def nuevo_producto():
 producto= input("Ingrese el nombre del producto: ")
 cod= int(input("Ingrese el codigo del producto: "))
 cant_producto= input("Ingrese la cantidad de productos a agregar:")
 descrip=input("Ingrese la descripcion del producto: ")
 
 productos[cod] = {
  "Producto: ": producto,
  "Codigo: ": cod,
  "Cantidad: ": cant_producto,
  "Descripción: ": descrip
 }
 print(f"Producto registrado. El código es: {cod}")
 return productos[cod]

def modificar_produc():
 cod=input("Ingrese el código del producto: ")
 if cod in productos:
  print("1 - Nombre")
  print("2 - Cantidad")
  print("3 - Descripción")
  opt_mod=input("Elija qué desea modificar: ")
  if (opt_mod)==1:
   producto=input("Ingrese el nuevo nombre")
  elif (opt_mod)==2:
   cant_producto=input("Ingrese la cantidad nueva: ")
  elif (opt_mod)==3:
   descrip=input("Elija la nueva decripcion")
  else:
   print("Elija opción válida")
   productos[cod] = {
  "Producto: ": producto,
  "Codigo: ": cod,
  "Cantidad: ": cant_producto,
  "Descripción: ": descrip
 }
 print("Cambio registrado")
 return productos[cod]

def eliminar_produc():
 cod=input("Ingrese el código del producto: ")
 if cod in productos:
  del productos[cod]
  print("El producto ha sido eliminado")
 return

def ver_stock(critico):
 
 for cod, producto in productos.items():
        if producto['Cantidad'] < critico:
            print(f"Codigo: {cod}, Producto: {producto['Producto']}, Cantidad: {producto['Cantidad']}")


