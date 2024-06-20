'''
Calcular comisiones creando un programa que le pregunte al usuario su nombre y cuánto ha vendido en este
mes. El programa le va a responder con una frase que incluya su nombre y el monto que le corresponde por las comisiones.
'''

nombre = input("Ingrese su nombre: ")
ventas_totales = float(input("Ingrese sus ventas totales: "))

commission = round(ventas_totales * 13 / 100, 2)

print(f"Hola {nombre}. Sus ventas fueron de {ventas_totales}, Las comisiones por esas ventas son de ${commission}")

