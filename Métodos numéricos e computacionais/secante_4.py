from numpy import linspace
import sympy
import sys

# Definicao da variahvel que serah lida
x = sympy.symbols('x')

# O usuario entra com uma funcao da escolha
func = input("Entre com uma funcao f(x): (x**2 -> x ao quadrado): ")


# Cria uma funcao inline que leh a entrada do usuahrio 
f = lambda x: eval(func) 


# x0  -  ponto inicial 
# TOL -  Tolerancia
# N   -  Numero mahximo de iteracoes 

# Calcular a derivada da funcao


# Funcao que irah calcular o mehtodo
def secante(f, x0, x1, TOL, N):

  i = 1

  # Calcular f(x0) e f'(x0)
  # Chama a funcao inline f
  fx0 = f(x0)

  # Calcula a primeira iteracao do Mehtodo de Newton 
  z_2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
  #xt = z_2
  
  # Calcula o valor de f no ponto z
  fx = f(z_2)

  # Primeiro critehrio de parada, calcular o intervalo
  intervalo = abs(z_2-x0)

  # Segundo critehrio de parada, se |f(x)| < TOL
  erro2 = abs(fx)

  z_1 = x1

  while intervalo > TOL and erro2 > TOL  and i <= N:  

    fx0 = f(x0)

    z = z_2 - f(z_2)*(z_2 - z_1)/(f(z_2) - f(z_1)+0.0000001)
    z_1 = z_2
    z_2 = z

    fx = f(z)

    print("\n\n-----------------------------------------------------------------------------------------------------------------------------")
    print(" iteracao |  x(i)           | x(i+1)            |erro 1 = |x(i+1)-x(i)|  |  erro 2 = |f(x(i+1))|                          ") 
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("   %d      | x(%d)=%10.8f | x(%d)=%10.8f   | |x(%d)-x(%d)|=%10.8f | f(x(%d))=%10.8f  |  \n\n"% (i,i-1,x0,i,z,i,i-1,intervalo,i,abs(fx)))        

    #Condicao de parada
    if (abs(fx) < TOL):
      print("O ponto x eh solucao\nA solucao foi obtida atravehs da imagem de f(x)\nO valor da solucao eh x = %8.10f e f(x) = %8.10f"%(z,fx))
      intervalo = linspace(z-20,z+20)

    i = i + 1

    intervalo = abs(z - x0)

    if (i >= N):  
      print('Nuhmero mahximo de iteracoes excedido')

    if intervalo < TOL:
          print('O ponto x eh solucao')
          print('\n\nA solucao foi obtida atravehs do domihnio de f(x)')
          print('\n\nO Valor da solucao eh:  x = %8.6f e f(x) = %8.6f'%(x,fx))

          
# Funcao MAIN 
if __name__ == "__main__":       
  x0  = float(input("Entre com o ponto inicial (x0): "))
  x1  = float(input("Entre com o ponto inicial (x1): "))
  TOL = float(input("Entre com a tolerancia: "))
  N   = int(input("Entre com o nuhmero mahximo de iteracoes: ")) 

  secante(f, x0, x1, TOL, N)


#########################################################
###                                                   ###
###             EXEMPLO DE ENTRADA:                   ###
###      "x**2 + 5*x - 4" ou  "cos(x)* x**2"          ###
###                                                   ###
###   USAR AS ASPAS PARA O COHDIGO ENTENDER A ENTRADA ###
###             COMO ENTRADA STRING                   ###
###                                                   ###
#########################################################

"""
expressao f(x) : "x**2 + 4*x - 4"
x elevado na 2 mais 4 vezes x menos 4 
"""
