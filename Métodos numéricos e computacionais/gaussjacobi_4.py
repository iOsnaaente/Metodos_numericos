# Bibliotecas de manipulacao matemahtica
from numpy import linalg as LA
import numpy as np
from math import *

#########################################################
###                                                   ###
###             EXEMPLO DE ENTRADA:                   ###
###		                                              ###
###   USAR AS ASPAS PARA O COHDIGO ENTENDER A ENTRADA ###
###             COMO ENTRADA STRING                   ###
###                                                   ###
###         tamanho da matriz quadrada                ###
###                      2                            ###
###                                                   ###
###           Valores da matriz 2x2:                  ###
###                   " 2 3 "                         ###
###                   " 3 5 "                         ###
###                                                   ###
###           Valores dos vetores:                    ###
###                   " 2 5"                          ###
###                   " 5 5"                          ###
###                                                   ###
#########################################################

if __name__ == "__main__":

	t = int(input("Tamanho da matriz A:"))
	A = np.array([list(map(float,input("linha "+str(x+1)+":").split())) for x in range(t)])
	b = np.array([[x] for x in list(map(float,input('Digite os valores do vetor b: ').split()))])
	xv = np.array([x for x in list(map(float,input('Digite os valores do vetor x0: ').split()))])

	E = float(input('Digite o erro: '))
	NMax = int(input('Digite o numero mahximo de interacoes: '))

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

		#mehtodo iterativo
		while erro > E and n < NMax:
			XN = np.dot(C,xv)+g
			erro = LA.norm(np.subtract(XN,xv),inf)/LA.norm(XN,inf)
			xv = XN
			n = n + 1

		print('Solucao: '+str(xv)+' Erro: '+str(erro))

	else:
		print('Nao hah convergehncia, use outra Matriz')