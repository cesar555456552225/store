import requests

def main():
    while True:
        print("\nBienvenido al sistema de gestión de mi tienda.")
        print("1. Consultar productos.")
        print("2. Consultar un producto en específico.")
        print("3. Crear un nuevo producto.")
        print("4. Actualizar un producto.")
        print("5. Eliminar un producto.")
        print("6. Salir del programa.")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            consultar_productos()
        elif opcion == "2":
            consultar_productos_por_id()
        elif opcion == "3":
            crear_producto()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            print("Hasta luego")
            break
        else:
            print("Opción inválida.")


def consultar_productos():
    url = "https://api.escuelajs.co/api/v1/products"
    response = requests.get(url)
    if response.status_code == 200:
        datos = response.json()
        for producto in datos:
            id = producto.get("id")
            titulo = producto.get("title")
            precio = producto.get("price")
            categoria = producto.get("category", {}).get("name")
            print(f"\nID: {id}")
            print(f"Nombre: {titulo}")
            print(f"Precio: {precio}")
            print(f"Categoria: {categoria}")
    else:
        print("Error en el proceso.")

def consultar_productos_por_id():
    id_usuario = int(input("Indique el ID del producto: "))
    url=f"https://api.escuelajs.co/api/v1/products/{id_usuario}"

    response = requests.get(url)
    if response.status_code ==200:
        datos = response.json()

        id = datos.get("id")
        titulo = datos.get("title")
        precio = datos.get("price")
        categoria = datos.get("category", {}).get("name")
        print(f"\nID: {id}")
        print(f"Nombre: {titulo}")
        print(f"Precio: {precio}")
        print(f"Categoria: {categoria}")
    else:
        print("Error en el proceso")

def crear_producto():
    titulo = input("Ingrese el nombre del producto: ")
    precio = int(input("Ingrese el pecio del producto: "))
    descripcion = input("ingrese una descripcion para el producto: ")
    categoria_id= int(input("Ingrese el ID de la categoria del producto: "))
    imagenes = input("Ingrese una url de la imagen: ")

    url="https://api.escuelajs.co/api/v1/products"
    producto={
        "title": titulo,
        "price": int(precio),
        "description": descripcion,
        "categoryId": int(categoria_id),
        "images":[imagenes],
    }

    response = requests.post(url, json=producto)

    if response.status_code ==201:
        print("El producto se creo exitosamente")
        print("Respuesta en json: ", response.json())
    else:
        print("No se pudo crear el producto", response.text)



def actualizar_producto():
    id_buscar=int(input("Ingrese el id del producto que quiere actualizar: "))
    titulo = input("Ingrese el nuevo nombre del producto: ")
    precio = int(input("Ingrese el nuevo precio del producto: "))
    descripcion = input("ingrese una descripcion para el producto: ")
    categoria_id= int(input("Ingrese el ID de la categoria del producto: "))
    imagenes = input("Ingrese una url de la imagen: ")

    url=f"https://api.escuelajs.co/api/v1/products/{id_buscar}"

    producto = {
        "title":titulo,
        "price":int(precio),
        "description":descripcion,
        "categoryId":int(categoria_id),
        "images":[imagenes],
    }
    response = requests.put(url, json=producto)

    if response.status_code == 200:
        print("El produto se actualizo con exito.")
        print("Respuesta en json: ", response.json())
    else:
        print("Error, No se pudo actualizar el producto.")
        print("Respuesta: ", response.text)


def eliminar_producto():
    id_eliminar = int(input("Indique el id del producta a eliminar: "))
    url = f"https://api.escuelajs.co/api/v1/products/{id_eliminar}"
    response= requests.delete(url)
    if response.status_code == 200:
        print("El producto fue eliminado.")
    else:
        print("No se pudo eliminar el producto.")
        print("Respuesta: ", response.text)
main()