# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:41:55 2020

@author: Luís
"""

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


x0 = 0.7 
x1 = 0.8 
e  = 10**-6 

def f(x):
    return math.cos(x) - x

it = 2
d = e + 1
resultados = []

while d > e:
    
    xn = x1 - (f(x1) * (x1 - x0))/(f(x1) - f(x0))
    resultados.append(xn)

    print("x{}:\t{}".format(it, xn))
    
    d = math.fabs(xn - x1)
    
    x0 = x1
    x1 = xn
    it = it + 1

ordemconvergencia(resultados[-4],resultados[-3],resultados[-2],resultados[-1])