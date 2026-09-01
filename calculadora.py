# Funciones básicas de la calculadora
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    # Retorna el producto de dos números
    return a * b

def dividir(a, b):
    # Retorna la división protegiendo contra división por cero
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

# Casos de prueba
print("Suma 5 + 3 =", sumar(5, 3))
print("Resta 10 - 4 =", restar(10, 4))
print("Multiplicación 4 * 3 =", multiplicar(4, 3))
print("Multiplicación 8 * 0 =", multiplicar(8, 0))
print("División 10 / 2 =", dividir(10, 2))
print("División 10 / 0 =", dividir(10, 0))
