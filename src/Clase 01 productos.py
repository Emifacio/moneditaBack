# -------------------------------------------------------------------
# Escribimos una serie de funciones para crear una pequeña app que
# maneje un arreglo que contenga datos de productos.
# Cada producto tiene un código numérico entero, una descripción
# alfabética, una cantidad en stock y un precio de venta.
# Nuestro producto también incluye una imagen y un proveedor.
# Nuestras funciones harán lo siguiente:
#
# - Agregar un producto al arreglo
# - Consultar un producto a partir de su código
# - Modificar los datos de un producto a partir de su código
# - Obtener un listado de los productos que existen en el arreglo.
# - Eliminar un producto del arreglo
# -------------------------------------------------------------------

# Definimos una lista para almacenar los productos.
# Es una lista de diccionarios.
productos = []

# -------------------------------------------------------------------
# Función para agregar un producto al arreglo
# --------------------------------------------------------------------
def agregar_producto(codigo, descripcion, cantidad, precio, imagen, proveedor):
   
 
    # Verificamos si ya existe un producto con el mismo código.
    if consultar_producto(codigo):
        
        return False  # Ya existe un producto con el mismo código, no se agrega.

    # Si no existe, creamos un diccionario con los datos del producto...
    nuevo_producto = {
        'codigo': codigo,            # Asigna el valor del argumento 'codigo' al atributo 'codigo' del nuevo producto.
        'descripcion': descripcion,  # Asigna el valor del argumento 'descripcion' al atributo 'descripcion' del nuevo producto.
        'cantidad': cantidad,        # Asigna el valor del argumento 'cantidad' al atributo 'cantidad' del nuevo producto.
        'precio': precio,            # Asigna el valor del argumento 'precio' al atributo 'precio' del nuevo producto.
        'imagen': imagen,            # Asigna el valor del argumento 'imagen' al atributo 'imagen' del nuevo producto.
        'proveedor': proveedor       # Asigna el valor del argumento 'proveedor' al atributo 'proveedor' del nuevo producto.
    }
    # Y lo agregamos a nuestro arreglo.
    productos.append(nuevo_producto) # Agrega el nuevo producto a la lista 'productos'.
    return True                      # Retorna True para indicar que la operación se completó exitosamente.

# -------------------------------------------------------------------
# Función para consultar un producto a partir de su código
# -------------------------------------------------------------------
def consultar_producto(codigo):
    """
    Consulta un producto a partir de su código y devuelve sus datos.

    Parámetros:
    - codigo: int, código numérico del producto.

    Retorna:
    - dict: datos del producto en forma de diccionario, o False si no se encontró el producto.
    """
    # Recorremos la lista de productos...
    for producto in productos:
        # Y si el código es el correcto,
        if producto['codigo'] == codigo:
            # Regresamos el diccionario correspondiente.
            return producto
    # Si el bucle finaliza sin encontrar el producto,
    # regresamos "falso."
    return False

# -------------------------------------------------------------------
# Función para modificar los datos de un producto a partir de su código
# -------------------------------------------------------------------
def modificar_producto(codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
    """
    Modifica los datos de un producto a partir de su código.

    Parámetros:
    - codigo: int, código numérico del producto.
    - nueva_descripcion: str, nueva descripción alfabética del producto.
    - nueva_cantidad: int, nueva cantidad en stock del producto.
    - nuevo_precio: float, nuevo precio de venta del producto.
    - nueva_imagen: str, nueva imagen del producto.
    - nuevo_proveedor: int, nuevo número de proveedor del producto.
    """
    # Recorremos la lista de productos...
    for producto in productos:
        # Y si el código es el correcto,
        if producto['codigo'] == codigo:
            # ...actualizamos los valores de cada clave del diccionario
            producto['descripcion'] = nueva_descripcion
            producto['cantidad'] = nueva_cantidad
            producto['precio'] = nuevo_precio
            producto['imagen'] = nueva_imagen
            producto['proveedor'] = nuevo_proveedor

            # Como no hay otro producto con ese código, salimos del bucle.
            return True
    # Si llegamos aquí, el producto no existe.
    return False

# -------------------------------------------------------------------
# Función para obtener un listado de los productos en pantalla
# -------------------------------------------------------------------
def listar_productos():
    """
    Muestra en pantalla un listado de los productos existentes.
    """
    # Recorremos la lista de productos...
    print("-" * 50)
    for producto in productos:
        # Y mostramos los datos de cada uno de ellos.
        print(f"Código: {producto['codigo']}")
        print(f"Descripción: {producto['descripcion']}")
        print(f"Cantidad: {producto['cantidad']}")
        print(f"Precio: {producto['precio']}")
        print(f"Imagen: {producto['imagen']}")
        print(f"Proveedor: {producto['proveedor']}")
        print("-" * 50)

# -------------------------------------------------------------------
# Función para eliminar un producto a partir de su código
# -------------------------------------------------------------------
def eliminar_producto(codigo):
    """
    Elimina un producto a partir de su código.

    Parámetros:
    - codigo: int, código numérico del producto.
    """
    # Recorremos la lista de productos...
    for producto in productos:
        # Y si el código es el correcto,
        if producto['codigo'] == codigo:
            # ...lo quitamos de la lista.
            productos.remove(producto)
            # Como no hay otro producto con ese código, salimos del bucle.
            return True
    # Si llegamos aquí, el producto no existe.
    return False

# -------------------------------------------------------------------
# Ejemplo de uso de las funciones
# -------------------------------------------------------------------

# Agregamos productos a la lista:
agregar_producto(1, 'Teclado USB 101 teclas', 10, 4500, 'teclado.jpg', 101)
agregar_producto(2, 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg', 102)
agregar_producto(3, 'Monitor LCD 22 pulgadas', 15, 52500, 'monitor22.jpg', 103)
agregar_producto(4, 'Monitor LCD 27 pulgadas', 25, 78500, 'monitor27.jpg', 104)
agregar_producto(5, 'Pad mouse', 5, 500, 'padmouse.jpg', 105)

# Eliminamos un producto del stock.
#eliminar_producto(5)  


# Consultar un producto por su código
# producto = consultar_producto(1)
# if producto:
#     print(f"Producto encontrado: {producto['descripcion']}")
# else:
#     print("Producto no encontrado.")

# Modificar un producto por su código
# modificar_producto(1, 'Teclado mecánico 62 teclas', 20, 34000, 'tecladomecanico.jpg', 106)

# Listamos todos los productos en pantalla
listar_productos()
