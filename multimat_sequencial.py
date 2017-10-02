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
		print (dimension is not )
		try:
			if dimension>0:
				self.__dimension=dimension
			else: raise ValueError("Value of dimension must be an integer greater than 0")
		except Exception as e:
			raise e
		
		self.__matrix=[[0 for row in range(self.__dimension)] for col in range(self.__dimension)]
	
	def modifyRow(self, row, position):
		"""
		Modify a matrix row at position

		*row* is a list which represents a row of matrix. It must have the size equal to matrix dimension

		*position* is which row will be modified. It must be on [0, dimension)

		ValueError is raised if some parameter is not expected
		"""
		try: 
			if len(row) == self.__dimension 
				if position>=0 and position <self.__dimension:
					self.__matrix[position]=row
				else: 
					raise ValueError("The value of position=%d is out of range", position)
			else:
				raise ValueError("The row argument=%d is wrong", argument)
		except Exception as e:
			raise e

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
		print ("==============")
		for i in self.__matrix:
			print (self.__matrix[i])
		print ("==============")

	def __getitem__(self,arg):
		"""
		Override object.__getitem__(self)

		See more: hhttps://docs.python.org/3/reference/datamodel.html#object.__getitem__

		Return a list that is a copy from the *arg* row of matrix (arg )
		Return an element from matrix if 
		"""
		errostr=""
		try:
			x,y=arg
			return self.__matrix[x][y]
		except TypeError as err:
			errostr+="arg="+str(arg)+" is not a tuple"
			try: return self.__matrix[arg].copy()
			except TypeError as e:
				errostr+= " and arg is not an integer"
				raise ValueError(errostr)
			except IndexError as e:
				raise e
		except IndexError as e:
			raise e
	
	def __setitem__(self,arg,value):
		"""
		Override object.__setitem__(self)
		
		See more: hhttps://docs.python.org/3/reference/datamodel.html#object.__setitem__

		Modify an specific element from matrix
		"""
		try:
			x,y=arg
			return self.__matrix[x][y]=value
		except TypeError as err:
			errostr+="arg="+str(arg)+" is not a tuple"
			try: return self.__matrix[arg].copy()
			except TypeError as e:
				errostr+= " and arg is not an integer"
				raise ValueError(errostr)
			except IndexError as e:
				raise e

def matrixmult(A,B):
	"""
	Multiplies matrices
	raises RuntimeError
	"""
	if A is not SquareMatrix or B is not SquareMatrix or len(A)!=len(B):
		raise ValueError("The dimensions of matrices must be same")
	C=SquareMatrix(len(A))

	for i in range(len(A)):
		for j in range(len(B)):
			result=0
			for k in range(len(A)):
				soma+=A[i,k]*B[k,j]
			C[i,j]=soma
	return C

A=SquareMatrix(2)
for i in range(len(A)):
	A[i,0]=1
	A[i,0]=2
B=SquareMatrix(2)
for i in range(len(A)):
	A[i,0]=2
	A[i,0]=1

print(A,B)
print(matrixmult(A,B))