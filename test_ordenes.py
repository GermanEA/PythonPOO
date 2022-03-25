from Producto import Producto
from Orden import Orden

producto1 = Producto('Camisa', 100.00)
producto2 = Producto('Pantalón', 150.00)
productos1 = [producto1, producto2]
producto3 = Producto('Calcetines', 50.00)
producto4 = Producto('Blusa', 70.00)
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
orden2 = Orden(productos2)
print(orden1)
print(orden2)
print(f'Total Orden 1: {orden1.calcular_total()}')
print(f'Total Orden 2: {orden2.calcular_total()}')
