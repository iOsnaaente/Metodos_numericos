import numpy as np
import matplotlib.pyplot as plt 

#A função já está definida aqui
def f(x): return x**2-2

# a - extremo esquedo 
# b - extremo direito 
# TOL - tolerância
# N - numero máximo de iterações

def bissecao(f,a,b,TOL,N):  
    i = 1
    fa = f(a)  
    fb = f(b)
    intervalo = abs(b-a)
    while intervalo > TOL and i<=N:  
        #iteracao da bissecao  
        pm = (a+b)/2  
        fpm = f(pm)  
        #condicao de parada  
        if abs(fpm) < TOL:  
            return print('O ponto médio é solução\nA solução foi obtida através da imagem de f(x)\nO valor da solução é: pm = %8.6f e f(x) = %8.6f'% (pm,fpm))

        print('\n\n------------------------------------------------------------------------------------------------------------------------------')
        print(' iteracao |     a    |     f(a)     |     b     |   f(b)    |   pm   |  f(pm)  | erro 1(b-a) | erro 2(f(pm))                          ')
        print('-------------------------------------------------------------------------------------------------------------------------------\n');
        print('   %d      | %f | %8.6f  |  %8.6f  | %8.6f  | %8.6f | %8.6f | %8.6f | %8.6f  \n\n '% (i,a,f(a),b,f(b),pm,f(pm),(b-a),abs(f(pm))))

        i = i + 1 
        #bissecta o intervalo  
        if (fa * fpm > 0):  
            a = pm  
            fa = fpm  
        else:  
            b = pm  
        intervalo = abs(b-a)

    if (i >= N): return print('Numero máximo de iterações excedido')
    if intervalo < TOL:
        print('O ponto médio é solução')
        print('\n\nA solução foi obtida através do domínio de f(x)')
        print('\n\nO Valor da solução é: x = %8.6f e f(x) = %8.6f'%(pm,fpm))

a = int(input("Entre com o ponto a: "))
b = int(input("Entre com o ponto b: "))
TOL = float(input("Entre com a tolerancia: "))
N = int(input("Entre com o número máximo de iterações: "))

bissecao(f,a,b,TOL,N)
 
intervalo = np.linspace(a,b)
plt.plot(intervalo,f(intervalo))
plt.grid(); plt.show()
