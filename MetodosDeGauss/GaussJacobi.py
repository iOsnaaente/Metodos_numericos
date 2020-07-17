from numpy import zeros, linspace, array
from numpy.linalg import norm

def gaussJacobi(A, B, Ap, e):
    C = zeros((len(A), len(A)))
    g = zeros((len(B),1))

    # Construir as matrizes C e g 
    for i in range(len(A)):
        g[i] = B[i]/A[i][i]
        for j in range(len(A)):
            if i == j :
                C[i][j] = -A[i][j]/A[i][i]
    
    # Testando a condição de parada 
    if norm(C, 1) < 1:
        erro = 1        
        # Se quisermos saber quantas iterações foram feitas 
        #n = 0
        while erro > e:
            An = C*Ap + g
            erro = norm(An-Ap)/norm(An)
            Ap = An
            #n = n + 1
        
        return Ap 

    else:
        return None


if __name__ == '__main__':

    '''
    t  = int(input("Tamanho M da matriz A[MxM]:"))
    
    A  = [(map(float,input("linha "+str(x+1)+":").split())) for i in range(t)]
    A  = array(A)
    
    B  = [[x] for x in list(map(float,input('Digite os valores do vetor B [Mx1]: ').split()))]
    B  = array(B)

    Ap = array([x for x in list(map(float,input('Digite os valores do vetor X[Mx1]: ').split()))])    
    
    e  = input("Entre com o erro máximo tolerado: ")
    '''

    t = 3
    A  = array([[10,2,1], [1,5,1], [2,3,10]])
    B  = array([7,-8,6])
    Ap = array([4,-1,1])
    e  = 0.00001  
    
    valores = gaussJacobi(A, B, Ap, e)

    if valores is not None:
    
        print('Os valores convergem no ponto ', end='')
        str_append = ''
        soma = 0 

        for i in range (len(valores)):
            str_append = str_append + "x%i: %10.8f" %(i, A[0][i]*valores[i])
            soma = soma + A[0][i]*valores[i]
        
        print(' y(x)=%10.8f onde:' %soma)
        print(str_append)
    
    else:
        print('Não há convergência!!!')