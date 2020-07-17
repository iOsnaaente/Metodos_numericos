#! /usr/bin/env python

from math import inf

#SOLUCAO DE EQUACOES

#Define a função 2x³ + x² -2x + 3   #-2 e -1 
def fun(x):
	return (x*(-1*x + 2)+4)


def zero(a,b, d=inf):

	e = 0.00000001
	p = float((a+b)/2)

	fa = fun(a)
	fb = fun(b)
	fp = fun(p)

	'''
	print("fa= {} fb= {} fp= {} dis= {}".format(fa,fb,fp,d))
	print("a= {} b= {} p= {}\n".format(a,b,p))

	print("a = {} fa = {} ".format(a,fa))
	print("p = {} fp = {} ".format(p,fp))
	print("b = {} fb = {} ".format(b,fb))
	print("d = {}\n".format(d))
	'''

	if d > e:
		if ((fa >= 0 and fp < 0) or (fa < 0 and fp > 0)):
			b = p
			d = b - a
			p = zero(a,b,d)

		elif ((fb >= 0 and fp < 0) or (fb < 0 and fp > 0)):
			a = p 
			d = b - a
			p = zero(a,b,d)

		else:
			return 'null'

	return p 


_zeros = []

#A menor que B 
def zeros(A,B, accuracy=1):
	if B < A:
		A, B = B, A
	n = 1
	for i in  range(int(A)*accuracy,int(B)*accuracy, 1):
		print("iteração: ", n)
		if zero(i/accuracy,(i+1)/accuracy) != 'null':
			_zeros.append(zero(i/accuracy,(i+1)/accuracy))
		n=n+1
	if _zeros == []:
		print("Não foi encontrado nenhum valor nulo no intervalo ({},{})".format(A,B))
	else:
		print("Os valor para zero da função são:\n{}".format(_zeros))


if __name__ == "__main__":

	zeros(-2,5)

