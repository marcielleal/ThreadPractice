#!/usr/bin/env python3

class SquareMatrix():
	"""
	Represent a square matrix
	The structure of matrix can not be changed, only values can be modified
	"""
	def __init__(self, dimension):
		"""
		Construct a list containing n lists of size=n, where n is the dimension argument

		*dimension* is the quantity of rows (or columns) of matrix

		ValueError is raised if the __dimension is not greater than 0
		"""
		self.__dimension=0
		if isinstance(dimension, int) and dimension>0:
			self.__dimension=dimension
		else: raise ValueError("Value of dimension must be an integer greater than 0")
		self.__matrix=[[0 for row in range(self.__dimension)] for col in range(self.__dimension)]

	def __len__(self):
		"""
		Override object.__len__(self)

		See more: https://docs.python.org/3/reference/datamodel.html#object.__len__
		"""
		return self.__dimension

	def __str__(self):
		"""
		Override object.__str__(self)

		See more: https://docs.python.org/3/reference/datamodel.html#object.__str__
		"""
		out="==============\n"
		for row in self.__matrix:
			out+=str(row)+"\n"
		out+="==============\n"
		return out
	def __getitem__(self,arg):
		"""
		Override object.__getitem__(self)

		See more: hhttps://docs.python.org/3/reference/datamodel.html#object.__getitem__

		Return a copy from a row of matrix if arg is an integer
		Return an element from matrix if arg is a tuple

		*arg* must be a tuple with two integers or only an integer, otherwise TypeError will be raised 
		The integers (x,y) that compose *arg* must be from [0,dimension), otherwise IndexError will be raised 
		"""
		if isinstance(arg,tuple):
			x,y=arg
			if(type(y) is int and type(x) is int):	#arg may be an slice and this would be a problem
				return self.__matrix[x][y]
			else: raise TypeError("*arg* "+str(arg)+" must be a tuple with two integers")
		elif isinstance(arg,int):
			return self.__matrix[arg].copy()
		else: raise TypeError("*arg* "+str(arg)+" must be a tuple or an integer")

	def __setitem__(self,arg,value):
		"""
		Override object.__setitem__(self)

		See more: hhttps://docs.python.org/3/reference/datamodel.html#object.__setitem__

		Modify an specific element from matrix

		*arg* must be a tuple with two integers, otherwise TypeError will be raised 
		The integers (x,y) that compose arg must be from [0,dimension), otherwise IndexError will be raised 
		"""
		if isinstance(arg,tuple):
			x,y=arg
			if(type(y) is int and type(x) is int):
				self.__matrix[x][y]=value
			else: raise TypeError("*arg* "+str(arg)+" must be a tuple with two integers")
		else: raise TypeError("*arg* "+str(arg)+" must be a tuple")
#End of SquareMatrix

def matrixmult(A,B):
	"""
	Multiplies matrices
	
	*A* and *B* must be instances from SquareMatrix class and they must have same dimensions, otherwise ValueError will be raised
	"""
	if type(A) is not SquareMatrix or type(B) is not SquareMatrix or len(A)!=len(B):
		raise ValueError("The dimensions of matrices must be same")
	C=SquareMatrix(len(A))

	for i in range(len(A)):
		for j in range(len(B)):
			result=0
			for k in range(len(A)):
				result+=A[i,k]*B[k,j]
			C[i,j]=result
	return C

def 

A=SquareMatrix(2)
for i in range(len(A)):
	A[i,0]=1
	A[i,1]=2
B=SquareMatrix(2)
for i in range(len(B)):
	B[i,0]=2
	B[i,1]=1

print(A,B)
print(matrixmult(A,B))