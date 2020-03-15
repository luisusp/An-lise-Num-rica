import math

p = float(input("Calcule a raiz quadrada de: "))
a = float(input("Digite o valor do intervalo inicial: "))
b = float(input("Digite o valor do intervalo final: "))

e = 0.00001

def f(x):
	return x**2 - p

if f(a)*f(b) < 0:
	while (math.fabs(b-a)/2 > e):
		xi = (a+b)/2
		if f(xi) == 0:
			print("A raiz é:" ,xi)
			break
		else:
			if f(a)*f(xi) < 0:
				b = xi
			else:
				a = xi
	print("O valor da raiz quadrada é: ", xi)
else:
	print("Neste intervalo não há raiz!")
