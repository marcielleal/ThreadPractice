#!/usr/bin/env python3

from threading import Thread
import squarematrix

def __rowmultmatrix(A,i,B,C):
	"""
	Multiply the i-th row of matrix *A* by matrix *B*, the result is putted on matrix *C*

	*A*, *B* and *C* must have the same dimensions
	*i* must be an integer from [0,len(A)), otherwise ValueError is raised 

	Others Exceptions can be raised by SquareMatrix.__getitem__ and SquareMatrix.__setitem__
	"""
	if(i>=0 and i<len(A)):
		for j in range(len(B)):
			result=0
			for k in range(len(A)):
				result+=A[i,k]*B[k,j]
			C[i,j]=result
		i+=1
	else: raise ValueError("i=%d is out of range"%i)


def __runThread(A,B,C,_start,numLines,totalNumThreads):
	"""

	"""
	for i in range(numLines):
		__rowmultmatrix(A,_start,B,C)
		_start+=totalNumThreads

def matrixmult(A,B,numOfThreads=None):
	"""
	Multiply matrices
	
	*A* and *B* must be instances from SquareMatrix class and they must have same dimensions, otherwise ValueError will be raised
	*numOfThreads* ........
	If numOfThreads <=1, this function will ignore numOfThreads
	"""
	
	if type(A) is not squarematrix.SquareMatrix and type(B) is not squarematrix.SquareMatrix and len(A)!=len(B):
		raise ValueError("matrices dimensions must be same")

	C=squarematrix.SquareMatrix(len(A))
	if type(numOfThreads) is not int or numOfThreads<=1:
		for i in range(len(A)):
			__rowmultmatrix(A,i,B,C)
	else:
		numLinesByThread=0
		numThreadWithAdd=0

		if(numOfThreads<len(A)):
			numLinesByThread=int(len(A)/numOfThreads)
			numThreadWithAdd=len(A)%numOfThreads
		else:
			numLinesByThread=1
			numOfThreads=len(A)
		
		threadList=[]

		for i in range(numOfThreads):
			if(numThreadWithAdd>0):
				_thread=Thread(name="Thread %d"%i,target=__runThread,args=(A,B,C,i,numLinesByThread+1,numOfThreads))
				_thread.start()
				threadList.append(_thread)
			else:
				_thread=Thread(name="Thread %d"%i,target=__runThread,args=(A,B,C,i,numLinesByThread,numOfThreads))
				_thread.start()
				threadList.append(_thread)
			numThreadWithAdd-=1
		
		for thread in threadList:
			thread.join()

	return C

