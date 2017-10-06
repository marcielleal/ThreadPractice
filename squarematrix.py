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
		elif dimension:
			self.__dimension=dimension
		else:
			raise ValueError("At least one argument is necessary")

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
		"""
		Override object.__str__(self)

		See more: https://docs.python.org/3/reference/datamodel.html#object.__repr__
		"""
		return self.__str__()
	def __getitem__(self,arg):#TODO see if arg need to be integer
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
			if(type(y) is int and type(x) is int):	#arg may be a slice and this would be a problem
				return self.__matrix[x][y]
			else: raise TypeError("*arg* "+str(arg)+" must be a tuple with two integers")
		else: raise TypeError("*arg* "+str(arg)+" must be a tuple")

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
			if(type(y) is int and type(x) is int):	#y and x cannot be slices
				self.__matrix[x][y]=value
			else: raise TypeError("*arg* "+str(arg)+" must be a tuple with two integers")
		else: raise TypeError("*arg* "+str(arg)+" must be a tuple")
#End of SquareMatrix
