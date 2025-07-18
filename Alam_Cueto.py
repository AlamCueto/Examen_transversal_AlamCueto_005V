productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
}

#Ver stock por marca
def Stock_marca(marca):
    marca = marca.lower()
    total_stock=0
    for modelo in productos:
        if productos[modelo][0].lower()==marca:
            total_stock += stock[modelo][1]
            print(f"Stock total de {marca}: {total_stock}")

#Busqueda de precio       
def busqueda_precios(precio_min, precio_max):
    try:
        precio_min=int(precio_min)
        precio_max=int(precio_max)
        resultados=[]
        for modelo in stock:
            precio,inventario=stock[modelo]
            if precio_min <= precio <= precio_max and inventario >0:
                marca=productos[modelo][0]
                tipo=productos[modelo][1]
                resultados.append(f"{marca}--{modelo}")
            if resultados:
                for r in sorted(resultados):
                    print(r)
        else:
            print("No hay producto con ese rango de precio")
    except ValueError:
        print("Debe ingresar valores enteros")


#Actualizar precios
def actualizar_precios(modelo,nuevo_precio):
    if modelo in stock:
        stock[modelo][0]=nuevo_precio
        return True
    return False


#Menú

def menu_tecnologico():
    while True:
        print("***** Menú Tecnologico *****")
        print("1. Ver stock")
        print("2. Buscar producto por precio ")
        print("3. Actualizar Precio")
        print("4. Salir")
        opción=input("Ingrese una opción a elegir:  ")
        if opción=="1":
            marca=input("Ingrese una marca de computador: ")
            Stock_marca(marca)
        elif opción=="2":
            precio_min =input("Ingrese precio mínimo: ")
            precio_max=input("Ingrese precio maximo: ")
            busqueda_precios(precio_min, precio_max)
        elif opción=="3":
            while True:
                try:
                    modelo=input("Ingrese modelo actualizar precio : ")
                    nuevo_precio=int(input("Ingrese el nuevo precio: "))
                    if actualizar_precios(modelo,nuevo_precio):
                        print("Precio actualizado correctamente")
                    else:
                        print("El modelo no existe")
                    continuar=input("Desea actualizar otro precio (si/no): ").lower()
                    if continuar !="si":
                        break
                except ValueError:
                    print("Debe ingresar un precio válido")
                    continuar=input("Desea actualizar otro precio (si/no): ").lower()
                    if continuar !="si":
                        break
        elif opción=="4":
            print("Programa Finalizado")
            break
        else:
            print("Opción invalida ")


#Ejectuar nuestro menú 
menu_tecnologico()