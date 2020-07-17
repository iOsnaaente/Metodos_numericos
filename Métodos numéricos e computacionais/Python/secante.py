#from __future__ import division
from numpy import *
import sympy  
import scipy.misc as sci
import matplotlib.pyplot as plt
x = sympy.symbols('x')

#Defina a funcao 

func = input("Entre com uma função (ex: cos(x),x**2 ...): ")

f = lambda x: eval(func) 

# x0 - ponto inicial 
# TOL - Tolerancia
# N - Numero máximo de iterações 

# Calcular a derivada da função


def newton(f,x0,x1,TOL,N):
    i = 1
    # Calcu2lar f(x0) e df(x0)/dx
    fx0 = f(x0)

    # Calcula a primeira iteração do Método de Newton 

    z_2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))

    # Calcula o valor de f no ponto z
    fx = f(z_2)

    # Primeiro critério de parada, calcular o intervalo
    intervalo = abs(z_2-x0)

    # Segundo critério de parada, se |f(x)| < TOL

    erro2 = abs(fx)
    
    z_1 = x1

    while intervalo > TOL and erro2 > TOL  and i <= N:  
       
        fx0 = f(x0)

        z = z_2 - f(z_2)*(z_2 - z_1)/(f(z_2) - f(z_1))

        z_1 = z_2
        z_2 = z

        fx = f(z)

        print("\n\n-----------------------------------------------------------------------------------------------------------------------------")
        print(" iteracao |  x(i)           | x(i+1)            |erro 1 = |x(i+1)-x(i)|  |  erro 2 = |f(x(i+1))|                          ") 
        print("-------------------------------------------------------------------------------------------------------------------------------")
        print("   %d      | x(%d)=%10.8f | x(%d)=%10.8f   | |x(%d)-x(%d)|=%10.8f | f(x(%d))=%10.8f  |  \n\n"% (i,i-1,x0,i,z,i,i-1,intervalo,i,abs(fx)))        

        #condicao de parada
        if (abs(fx) < TOL):
          print("O ponto x é solução\nA solução foi obtida através da imagem de f(x)\nO valor da solução é x = %8.6f e f(x) = %8.6f"%(z,fx))
          intervalo = linspace(z-20,z+20)
          plt.plot(z,f(z), 'go')
          plt.plot(intervalo,f(intervalo))
          plt.grid(); plt.show()

        i = i + 1

        intervalo = abs(z - x0)

    if (i >= N):  return print('Numero máximo de iterações excedido')
    if intervalo < TOL:
          print('O ponto x é solução')
          print('\n\nA solução foi obtida através do domínio de f(x)')
          print('\n\nO Valor da solução é:  x = %8.6f e f(x) = %8.6f'%(x,fx))

          intervalo = linspace(z-20,z+20)
          plt.plot(z,f(z), 'go')
          plt.plot(intervalo,f(intervalo))
          plt.grid(); plt.show()
      
x0 = float(input("Entre com o ponto inicial (x0): "))
x1 = float(input("Entre com o ponto inicial (x1): "))
TOL = float(input("Entre com a tolerancia: "))
N = int(input("Entre com o número máximo de iterações: ")) 

newton(f,x0,x1,TOL,N)


