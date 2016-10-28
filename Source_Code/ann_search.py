import os
import numpy as np
import pandas as pd
import cPickle
import compare
from annoy import AnnoyIndex


def search_img(img_path):

	rep_result = {}

	search_rep = compare.getRep(img_path)
	search_rep_test = list(search_rep)
	
	temp_search_rep = np.asarray(search_rep)
	temp_search_rep = search_rep*1000
	temp_search_rep = search_rep.astype(np.int32)
	temp_search_rep = abs(search_rep)
	

	
		

	ann_location = '../annoy'
	pkl_location = '../img_rep'
	annoy_list = os.listdir(ann_location)
	for x in range(len(annoy_list)):

		t = AnnoyIndex(128, metric = 'eucledian')

		ann_file = os.path.join(ann_location, annoy_list[x])
		
		temp = ann_file.split('/')
		temp = temp[-1]
		temp = temp.split('.')
		profile_id = temp[0]

		pkl_file = os.path.join(pkl_location, str(profile_id)) + '.pkl'

		t.load(ann_file)
		print len(temp_search_rep), x, profile_id
		n = t.get_nns_by_vector(temp_search_rep, 1, -1, True)
		print n
		index = n[0][0]

		raw_rep = open(pkl_file, 'rb')
		rep_list = cPickle.load(raw_rep)
		rep = rep_list[index]
		rep = np.asarray(rep)
		rep = list(rep)
		#print profile_id
		#print rep

		distance = search_rep - rep
		distance = format(np.dot(distance, distance))
		print distance

		rep_result[str(profile_id)] = distance
		#print rep_result
	print rep_result

if __name__ == '__main__':
	img_path = '../nisha_03.jpg'
	search_img(img_path)