# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:48:44 2020

@author: Luís
"""
import numpy as np

print("Seja f(x) = ax² + bx + c com a, b e c reais.")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

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

def newton(f,df,x0,e,maxiter=50):
    resultados=[]
 
    if abs(f(x0)) <= e:
        return x0, resultados
    print("k\t x0\t\t f(x0)")
    k=1
    while k<=maxiter:
        x1=x0-f(x0)/df(x0)
        resultados.append(x1)
        print("%d\t%e\t%e"%(k,x1,f(x1)))
        if abs(f(x1))<=e:
            return x1,resultados
        x0=x1
        k=k+1
    print("ERRO: Número máximo de iterações atingido")
    return x1,resultados
if __name__ =="__main__":
    def f(x):
        return a*x**2 + b*x + c
    def df(x):
        return 2*a*x + b
    
raiz, resultados = newton(f,df,1.5,0.0000000001)
ordemconvergencia(resultados[-4],resultados[-3],resultados[-2],resultados[-1])

print("A raiz é: ", raiz)
