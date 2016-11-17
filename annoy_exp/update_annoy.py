import os
import numpy as np
import pandas as pd
import cPickle
from annoy import AnnoyIndex

def create_annoy(profile_id):
	t = AnnoyIndex(128, metric = 'eucledian')
	count = 0

	annoy_location = '../annoy'
	annoy_path = os.path.join(annoy_location, str(profile_id)) + '.ann'

	pkl_location = '../img_rep'
	pkl_file = os.path.join(pkl_location, str(profile_id)) + '.pkl'
	try:
		data = open(pkl_file, 'rb')
		temp_rep = cPickle.load(data)
		for x in temp_rep:
			#x = np.asarray(x)		
			#x = x*10000
			#x = x.astype(np.int32)
			#x = abs(x)
			#print x
			t.add_item(count, x)
			count = count + 1

		t.build(100)
		t.save(annoy_path)
	except:
		pass

'''
if __name__ == "__main__":
	profile_id = 'test3t7hush'
	create_annoy(profile_id)
'''