import cPickle
import numpy as np

path = '../img_rep/nisha_03.pkl'

data = open(path, 'rb')

data = cPickle.load(data)
for x in range(len(data)):
	#print len(data[x])
	temp = np.asarray(data[x])
		
	temp = temp*1000
	

	temp = temp.astype(np.int32)
	temp = abs(temp)
	print len(temp)