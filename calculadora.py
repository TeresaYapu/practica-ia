def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

print("Suma 5 + 3 =", sumar(5, 3))
print("Resta 10 - 4 =", restar(10, 4))
print("División 10 / 2 =", dividir(10, 2))
print("División 10 / 0 =", dividir(10, 0))
