

def agregar_curso(codigo, descripcion, precio, imagen,
profesor):
if consultar_curso(codigo):
return False
nuevo_producto = {
'codigo': codigo,
'descripcion': descripcion,
'precio': precio,
'imagen': imagen,
'profesor': profesor
}
curso.append(nuevo_producto)
return True