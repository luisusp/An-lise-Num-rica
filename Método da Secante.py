import math

print("Seja f(x) = ax² + bx + c com a, b e c reais.")
a = float(input("Digite o valor de a: " ))
b = float(input("Digite o valor de b: " ))
c = float(input("Digite o valor de c: "))

x0 = float(input("Informe x0 de aproximação inicial: "))
x1 = float(input("Informe x1 de aproximação inicial: "))
e  = float(input("Informe a precisão: "))

def f(x):
    return (a * x**2) + (b * x) + c

it = 2

while True:
    
    xn = x1 - (f(x1) * (x1 - x0))/(f(x1) - f(x0))
    
    print("x{}:\t{}".format(it, xn))
    
    if math.fabs(xn - x1) < e:
        print("Raiz: ", xn)
        break
    else:
        x0 = x1
        x1 = xn
        it = it + 1
