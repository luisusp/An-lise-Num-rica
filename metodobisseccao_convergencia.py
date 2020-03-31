import math
import numpy as np

def ordemconvergencia(x0,x1,x2,x3):
  e3=abs((x3-x2))
  e2=abs((x2-x1))
  e1=abs((x1-x0))
  alpha1 = np.log(e3/e2) #ordemdeconvergencia
  alpha2 = np.log(e2/e1)
  ordemconvergencia = alpha1/alpha2
  lambida = (e3/(e1**ordemconvergencia)) #constade de erro
  print("Ordem de convergência é: ", ordemconvergencia)
  print("Constante de erro assintótica é: ", lambida)
  return()

def f(x):
    return x**3 - 26

a=2
b=4
erro = 10
resultados = []

while erro > 1e-8:
    c = (a+b)/2
    fa=f(a)
    fc=f(c)
    if fc == 0:
        raiz = c
        break
    elif fa * fc < 0:
        b = c
    else:
        a = c
    raiz = c
    resultados.append(c)
    erro = abs(fc)
print("A raiz é: ", raiz)

ordemconvergencia(resultados[-4],resultados[-3],resultados[-2],resultados[-1])