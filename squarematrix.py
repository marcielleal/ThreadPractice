#!/usr/bin/env python3

class SquareMatrix():
	"""
	Represent a square matrix
	The structure of matrix can not be changed, only values can be modified
	"""
	def __init__(self, dimension=None, file=None):
		"""
		Construct a list containing n lists of size=n, where n is the dimension argument

		*dimension* is the quantity of rows (or columns) of matrix (is ignored if file is not None)
		*file* is an _io.TextIOWrapper (a file object) of a file that contains a matrix.

		The file must to have the 2 integers on first line to represent matrix dimensions and
		each others lines have the matrix elements separeted by space 

		ValueError is raised if the obtained dimension is not greater than 0
		"""
		if file:
			self.__dimension=int(file.readline().split()[0])
		else:
			self.__dimension=dimension

		if self.__dimension<=0:
			raise ValueError("Value of dimension must be an integer greater than 0")
		
		self.__matrix=[[0 for row in range(self.__dimension)] for col in range(self.__dimension)]
		
		if file:
			i,j=0,0
			for line in file.readlines():
				for elem in line.split():
					self.__matrix[i][j]=int(elem)
					j+=1
				j=0
				i+=1

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
	def __repr__(self):
		return self.__str__()
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

def __rowmultmatrix(A,i,B,C,_range=None):
	"""
	Multiply the i-th row of matrix *A* by matrix *B*, the result is putted on matrix *C*
	If *_range* are setted, than all lines on [ith, _range-th) will be multiplied

	*A*, *B* and *C* must have the same dimensions
	*i* must be an integer from [0,len(A)), otherwise ValueError is raised 
	*_range* must be an integer greater than zero, otherwise it will be ignored


	Others Exceptions can be raised by SquareMatrix.__getitem__ and SquareMatrix.__setitem__
	"""
	if not _range or _range<1:
		_range=1

	if(type(i) is int and i>=0 and i<len(A)):
		while(_range>0):
			for j in range(len(B)):
				result=0
				for k in range(len(A)):
					result+=A[i,k]*B[k,j]
				C[i,j]=result
			i+=1
			_range-=1
	else:
		raise ValueError("i=%d is out of range")


import threading

def matrixmult(A,B,numOfThreads=None):
	"""
	Multiply matrices
	
	*A* and *B* must be instances from SquareMatrix class and they must have same dimensions, otherwise ValueError will be raised
	*numOfThreads* ........
	If numOfThreads <=1, this function will ignore numOfThreads
	"""
	if type(A) is SquareMatrix and type(B) is SquareMatrix and len(A)==len(B):
		if not numOfThreads or numOfThreads<=1:
			C=SquareMatrix(len(A))

			for i in range(len(A)):
				__rowmultmatrix(A,i,B,C)
		else:
			numLinesByThread=0
			numThreadWithAdd=0

			if(numOfThreads<len(A)):
				numLinesByThread=(len(A)/int(numOfThreads))
				numThreadWithAdd=len(A)%int(numOfThreads)
			else:
				numLinesByThread=1
				numOfThreads=len(A)

			threadList=[]

			for i in range(numOfThreads):
				currentLine=0
				if(numThreadWithAdd>0):
					threadList.add(threading.Thread(name=i,))
					currentLine-=numLinesByThread+1
				else:
					threadList.add(threading.Thread(name=i,))
					currentLine-=numLinesByThread
				numThreadWithAdd-=1


			for thread in threadList:
				thread.start()

			#TODO Barreira
		return C
	else: 
		raise ValueError("matrices dimensions must be same")
