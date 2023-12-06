from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()

app.config ['MYSQL_DATABASE_HOST'] = 'localhost'
app.config ['MYSQL_DATABASE_USER'] = 'root'
app.config ['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config ['MYSQL_DATABASE_DB'] = 'cursos'

mysql.init_app(app)

@app.route('/')
def index():
    
    conn = mysql.connect()
    cursor = conn.cursor()

    sql = "insert into cursos (nombre) value ('trading');"
    cursor.execute(sql)

    conn.commit(sql)

    return render_template('cursos/index.html')

if __name__ == '__main__':
    app.run(debug=True)


@app.route("/catalogo", methods=['POST'])
def crear_catalogo(): 
    codigo (int): El código del producto.
        descripcion = request.json
        cantidad = request.json
        precio = request.json
        imagen = request.json
        proveedor = request.json
        nombre= data["nombre de data que quiero"]
        cursor= mysql.cursor()
        cursor.execute("hacer la query a la bd")
        mysql.commit()
        cursor.close()
        return jsonify({'mensaje':'mensaje'}), 201
  #----------------------------------------------------------------
#     def agregar_producto(self, codigo, descripcion, cantidad, precio, imagen, proveedor):
#         """
#         Agrega un nuevo producto a la base de datos.

#         Args:
#             codigo (int): El código del producto.
#             descripcion (str): La descripción del producto.
#             cantidad (int): La cantidad en stock del producto.
#             precio (float): El precio del producto.
#             imagen (str): La URL de la imagen del producto.
#             proveedor (int): El código del proveedor.

#         Returns:
#             bool: True si el producto se agregó con éxito, False si ya existe un producto con el mismo código.
#         """
#         # Verificamos si ya existe un producto con el mismo código
#         self.conector.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
#         producto_existe = self.conector.fetchone()
#         if producto_existe:
#             return False

#         # Si no existe, agregamos el nuevo producto a la tabla
#         sql = f"INSERT INTO productos \
#                (codigo, descripcion, cantidad, precio, imagen_url, proveedor) \
#                VALUES \
#                ({codigo}, '{descripcion}', {cantidad}, {precio}, '{imagen}', {proveedor})"
#         self.conector.execute(sql)
#         self.conn.commit()
#         return True

#     #----------------------------------------------------------------
#     def consultar_producto(self, codigo):
#         """
#         Consulta un producto a partir de su código.

#         Args:
#             codigo (int): El código del producto a consultar.

#         Returns:
#             dict: Un diccionario con la información del producto o None si no se encuentra.
#         """
#         # Consultamos un producto a partir de su código
#         self.conector.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
#         return self.conector.fetchone()

#     #----------------------------------------------------------------
#     def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
#         """
#         Modifica los datos de un producto a partir de su código.

#         Args:
#             codigo (int): El código del producto a modificar.
#             nueva_descripcion (str): La nueva descripción del producto.
#             nueva_cantidad (int): La nueva cantidad en stock del producto.
#             nuevo_precio (float): El nuevo precio del producto.
#             nueva_imagen (str): La nueva URL de la imagen del producto.
#             nuevo_proveedor (int): El nuevo código del proveedor.

#         Returns:
#             bool: True si se realizó la modificación con éxito, False si no se encontró el producto.
#         """
#         # Modificamos los datos de un producto a partir de su código
#         sql = f"UPDATE productos SET \
#                     descripcion = '{nueva_descripcion}', \
#                     cantidad = {nueva_cantidad}, \
#                     precio = {nuevo_precio}, \
#                     imagen_url = '{nueva_imagen}', \
#                     proveedor = {nuevo_proveedor} \
#                 WHERE codigo = {codigo}"
#         self.conector.execute(sql)
#         self.conn.commit()
#         return self.conector.rowcount > 0

#     #----------------------------------------------------------------
#     def listar_productos(self):
#         """
#         Muestra en pantalla un listado de todos los productos en la tabla.
#         """
#         # Mostramos en pantalla un listado de todos los productos en la tabla
#         self.conector.execute("SELECT * FROM productos")
#         productos = self.conector.fetchall()
#         print("-" * 40)
#         for producto in productos:
#             print(f"Código.....: {producto['codigo']}")
#             print(f"Descripción: {producto['descripcion']}")
#             print(f"Cantidad...: {producto['cantidad']}")
#             print(f"Precio.....: {producto['precio']}")
#             print(f"Imagen.....: {producto['imagen_url']}")
#             print(f"Proveedor..: {producto['proveedor']}")
#             print("-" * 40)

#     #----------------------------------------------------------------
#     def eliminar_producto(self, codigo):
#         """
#         Elimina un producto de la tabla a partir de su código.

#         Args:
#             codigo (int): El código del producto a eliminar.

#         Returns:
#             bool: True si se eliminó el producto con éxito, False si no se encontró el producto.
#         """
#         # Eliminamos un producto de la tabla a partir de su código
#         self.conector.execute(f"DELETE FROM productos WHERE codigo = {codigo}")
#         self.conn.commit()
#         return self.conector.rowcount > 0

#     #----------------------------------------------------------------
#     def mostrar_producto(self, codigo):
#         """
#         Muestra los datos de un producto a partir de su código.

#         Args:
#             codigo (int): El código del producto a mostrar.
#         """
#         # Mostramos los datos de un producto a partir de su código
#         producto = self.consultar_producto(codigo)
#         if producto:
#             print("-" * 40)
#             print(f"Código.....: {producto['codigo']}")
#             print(f"Descripción: {producto['descripcion']}")
#             print(f"Cantidad...: {producto['cantidad']}")
#             print(f"Precio.....: {producto['precio']}")
#             print(f"Imagen.....: {producto['imagen_url']}")
#             print(f"Proveedor..: {producto['proveedor']}")
#             print("-" * 40)
#         else:
#             print("Producto no encontrado.")

# #--------------------------------------------------------------------
# # Ejemplo de uso con MariaDB
# catalogo = Catalogo(host='localhost', user='root', password='', database='miapp')

# # Agregamos productos a la tabla
# catalogo.agregar_producto(1, 'Teclado USB 101 teclas', 10, 4500, 'teclado.jpg', 101)
# catalogo.agregar_producto(2, 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg', 102)
# catalogo.agregar_producto(3, 'Monitor LED', 5, 25000, 'monitor.jpg', 102)

# # Consultamos un producto y lo mostramos
# producto = catalogo.consultar_producto(1)
# if producto:
#     print(f"Producto encontrado: {producto['descripcion']}")
# else:
#     print("Producto no encontrado.")

# # Modificamos un producto y lo mostramos
# catalogo.modificar_producto(1, 'Teclado mecánico', 20, 34000, 'tecmec.jpg', 106)
# catalogo.mostrar_producto(1)

# # Listamos todos los productos
# catalogo.listar_productos()

# # Eliminamos un producto
# # catalogo.eliminar_producto(2)
# # catalogo.listar_productos()