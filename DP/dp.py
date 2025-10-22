'edit distance'

import numpy as np
def ed(x,y):
	T = np.zeros(len(x)+1,len(y)+1,dtype=np.int32)
	for i in range(T.shape[0]):
		T[i,0]=i
	for j in range(T.shape[1]):
		T[i,0]=j
	for i in range(1,T.shape[0]):
		for j in range(1,T.shape[1]):
			T[i,j]=min(T[i-1,j]+1,T[i,j-1]+1,T[i-1,j-1]+x[[i-1]!=y[j-1]])
	return T
	
	