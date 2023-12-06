import mysql.connector
import json
# Instalar con pip install Flask
from flask import Flask, request, jsonify
from flask import request
# Instalar con pip install flask-cors
from flask_cors import CORS
# Instalar con pip install mysql-connector-python
import mysql.connector
# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename
# No es necesario instalar, es parte del sistema standard de Python
import os
import time

class Catalogo:

    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
            codigo INT,
            descripcion VARCHAR(255) NOT NULL,
            cantidad INT(4) NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            imagen_url VARCHAR(255),
            proveedor INT(2))''')
        self.conn.commit()

    def agregar(self,codigo,descripcion,cantidad,precio,imagen,proveedor):
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        producto_existe = self.cursor.fetchone()
        if producto_existe:
            return False
        
        # Si no existe el producto...

        self.cursor.execute(f"""INSERT INTO productos
        (codigo, descripcion, cantidad, precio, imagen_url,proveedor)
        VALUES ({codigo}, '{descripcion}', {cantidad}, {precio},'{imagen}', {proveedor})""")
        self.conn.commit()
        return True

    def eliminar(self,codigo):
        # Eliminamos un producto de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM productos WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0

    def modificar(self,codigo,descripcion,cantidad,precio,imagen,proveedor):
        # Modificamos los datos de un producto a partir de su código
        sql = f"""UPDATE productos SET
        descripcion = '{descripcion}',
        cantidad = {cantidad},
        precio = {precio},
        imagen_url = '{imagen}',
        proveedor = {proveedor}
        WHERE codigo = {codigo}"""
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def mostrarTodos(self):
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall()
        print("-" * 40)
        for producto in productos:
            print(f"Código.....: {producto['codigo']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen_url']}")
            print(f"Proveedor..: {producto['proveedor']}")
            print("-" * 40)

    def consultar_producto(self,codigo):
        # Consultamos un producto a partir de su código
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        return self.cursor.fetchone()

    def mostrarUno(self,codigo):
        # Mostramos los datos de un producto a partir de su código
        producto = self.consultar_producto(codigo)
        if producto:
            print("-" * 40)
            print(f"Código.....: {producto['codigo']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen_url']}")
            print(f"Proveedor..: {producto['proveedor']}")
            print("-" * 40)
        else:
            print("Producto no encontrado.")   

#-------------------------------- Programa Principal

catalogo = Catalogo(host = "localhost", user = "root", password = "root", database = "moneditaBack")

catalogo.agregar(1, 'Teclado USB 101 teclas', 10, 4500,'teclado.jpg', 101)
catalogo.agregar(2, 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg',102)
catalogo.agregar(3, 'Monitor LED', 5, 25000, 'monitor.jpg', 102)

codigo = int(input("Ingrese el codigo: "))
nombre = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad: "))
precio = int(input("Ingrese el precio: "))
imagen = input("Ingrese el texto de la imagen: ")
proveedor = int(input("Ingrese el proveedor: "))

catalogo.agregar(codigo,nombre,cantidad,precio,imagen,proveedor)
