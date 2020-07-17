from __future__ import division 
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import scipy.misc as sci
import numpy as np 
from numpy import linalg
from sympy import * 
import math as mt

x = symbols('x')

def trapezio(f):
    
    #Calculando derivadas

    #dfxa = abs(sci.derivative(f,a,dx=1.0,n=2))
    #dfxb = abs(sci.derivative(f,b,dx=1.0,n=2))

    aux = lambdify(x,abs(f.diff(x,2)))
    
    #Transformando o input em função 
    f = lambdify(x,f)

    #Verificando derivada máxima

    if aux(a) > aux(b):
        m2 = aux(a)
    else:
        m2 = aux(b)

    
    #Calculando numero n

    n = sqrt(((b-a)**3*m2)/(12*erro))

    n = int(mt.ceil(n))
    
    if  n % 2 == 0:
        n += 1

    #Criando n+1 pontons igualmente espaçados
    X = np.linspace(a,b,n)

    #Calculo do H
    h = (b - a) / n

    return  (h/2)*(f(X[0])+ 2*np.sum(f(X[1:n])) + f(X[-1]))

    
def um_terco(f):
    
    #Calculando derivadas

    #dfxa = abs(sci.derivative(f,a,dx=1.0,n=2))
    #dfxb = abs(sci.derivative(f,b,dx=1.0,n=2))

    aux = lambdify(x,abs(f.diff(x,4)))
    
    #Transformando o input em função 
    f = lambdify(x,f)

    #Verificando derivada máxima

    if aux(a) > aux(b):
        m2 = aux(a)
    else:
        m2 = aux(b)

    
    #Calculando numero n

    n = sqrt(((b-a)**5*m2)/(90*erro))

    n = int(mt.ceil(n))
    
    if  n % 2 == 0:
        n += 1

    #Criando n+1 pontons igualmente espaçados
    X = np.linspace(a,b,n)

    #Calculo do H
    h = (b - a) / n

    return  (h/3)*(f(X[0])+ 4*np.sum(f(X[1:n:2]))+2*np.sum(f(X[2:n:2])) + f(X[-1]))

qual = int(input("Qual integração numérica deseja, 1/3 de Simpson (1) ou regra de trapézios (2): "))

func = input("Entre com a funcao: ")
a = float(input("Entre com o ponto a: "))
b = float(input("Entre com o ponto b: "))
erro = float(input("Entre com o erro: "))


f = eval(func)

if qual == 1:
    print(um_terco(f))
elif qual == 2:
    print(trapezio(f))


