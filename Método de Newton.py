# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:48:44 2020

@author: Luís
"""
print("Seja f(x) = ax² + bx + c com a, b e c reais.")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

def newton(f,df,x0,e,maxiter=50):
  
    if abs(f(x0)) <= e:
        return x0
    print("k\t x0\t\t f(x0)")
    k=1
    while k<=maxiter:
        x1=x0-f(x0)/df(x0)
        print("%d\t%e\t%e"%(k,x1,f(x1)))
        if abs(f(x1))<=e:
            return x1
        x0=x1
        k=k+1
    print("ERRO: Número máximo de iterações atingido")
    return x1
if __name__ =="__main__":
    def f(x):
        return a*x**2 + b*x + c
    def df(x):
        return 2*a*x + b
raiz = newton(f,df,1.5,0.001)
print(raiz)
