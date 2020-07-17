from numpy import linalg as LA
import numpy as np 
from math import *

t = int(input("Tamanho da matriz A:"))
A = np.array([list(map(float,input("linha "+str(x+1)+":").split())) for x in range(t)])
b = np.array([[x] for x in list(map(float,input('Digite os valores do vetor b: ').split()))])
xv = np.array([x for x in list(map(float,input('Digite os valores do vetor x0: ').split()))])

E = float(input('Digite o erro: '))
NMax = int(input('Digite o numero maximo de interacoes: '))

# construindo matriz C e vetor g
C = np.zeros((t,t),dtype=float)
g = np.zeros(t,dtype=float)

for i in range(t):
	g[i] = b[i]/A[i][i]
	for j in range(t):
		if i != j:
			C[i][j] = -A[i][j]/A[i][i]

# norma da matriz:
if LA.norm(C,1) < 1:
	n=0
	erro=1
	#método iterativo
	while erro > E and n < NMax:
		XN = np.dot(C,xv)+g
		erro = LA.norm(np.subtract(XN,xv),inf)/LA.norm(XN,inf)
		xv = XN
		n += 1
	print('Solução: '+str(xv)+' Erro: '+str(erro))
else:
	print('Nao há convergência, use outra Matriz')