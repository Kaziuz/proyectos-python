import platform
import os

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    # Clase que hereda de la clase persona sus atributos y le añade # de cuenta y saldo
    def __init__(self, nombre, apellido, numero_cuenta, saldo_inicial):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial

    def __str__(self):
        # Método especial que en la instancia de la clase cuando se invoca el objeto print(cliente)
        # muestra sus atributos
        return f"""
            Cliente: {self.nombre} {self.apellido}
            cuenta: {self.numero_cuenta}
            saldo: {self.saldo}
        """

    def depositar(self, cantidad):
        # Agregar dinero al saldo
        self.saldo += cantidad
        return print(f"Depositados {cantidad} unidades. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        # Sacar/restar dinero del saldo
        if cantidad >= self.saldo:
            print(f"No es posible retirar {cantidad} de dinero. Supera su monto de {self.saldo} ")
        else:
            self.saldo -= cantidad
            return print(f"Retirados {cantidad} unidades. Nuevo saldo: {self.saldo}")

# ------------------------------------
# funciones que usa el programa
def def_clean_console():
    # Limpio la consola
    system = platform.system()  # obtengo el sistema operativo
    if system == "Darwin" or system == "Linux":
        os.system("clear")
    else:
        os.system("cls")  # Windows


def leer_datos_cliente():
    # Inicializamos el cliente
    print("\nPara iniciar crearemos su cuenta.")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese el número de cuenta: ")
    saldo = input("Ingrese su saldo inicial: ")
    return {
        "nombre": nombre,
        "apellido": apellido,
        "numero_cuenta": numero_cuenta,
        "saldo": saldo
    }


def leer_opt(mensaje):
    # Recibe un mensaje y lo muestra esperando una entrada
    return input(mensaje)


def mostrar_saldo(nombre, saldo):
    # Muestra el cliente actual con us estado de cuenta
    print(f"\nCliente {nombre}. Saldo actual: {saldo}\n")


def tablero_principal():
    # Muestra texto con elección para seguir
    print("""
        [1] - Depositar en su cuenta
        [2] - Retirar de su cuenta
        [3] - Salir del programa
    """)


def bienvenida():
    print("*" * 30)
    print(" Bienvenido a cuenta bancaria ")
    print("*" * 30)


def iniciar():
    # Método que corre el programa
    finalizar = False
    bienvenida()
    datos_cliente = leer_datos_cliente()
    cliente = Cliente(datos_cliente["nombre"], datos_cliente["apellido"], datos_cliente["numero_cuenta"],
                      int(datos_cliente["saldo"]))

    def_clean_console()
    while not finalizar:
        tablero_principal()
        nombre_completo = f"{cliente.nombre} {cliente.apellido}"
        mostrar_saldo(nombre_completo, cliente.saldo)
        opt = leer_opt("Ingrese una opción del tablero para continuar: ")
        if opt == "1":
            # Depositamos en la cuenta
            ingreso = leer_opt("Ingrese el monto a ingresar: ")
            cliente.depositar(int(ingreso))
            finalizar = False
            pass
        elif opt == "2":
            # Retiramos de la cuenta
            retiro = leer_opt("Ingrese el monto a retirar: ")
            cliente.retirar(int(retiro))
            finalizar = False
            pass
        else:
            # Salimos del programa
            print("Ha salido de cuenta bancaria")
            finalizar = True
            break

iniciar()
