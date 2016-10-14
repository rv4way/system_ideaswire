import os
import compare
import numpy as np
import pandas as pd
import csv
import cPickle

def search_img(image):

	rep_result_list = {}

	rep_location = '../img_rep'
	rep_file_list = os.listdir(rep_location)
	if rep_file_list == []:
		print 'DATABASE EMPTY'
		return 'DATABASE EMPTY'

	else:

		img_rep = compare.getRep(image)

		for x in range(len(rep_file_list)):
			name = rep_file_list[x]
			name = name.split('.')

			rep_file_path = os.path.join(rep_location, rep_file_list[x])
			pkl_data = open(rep_file_path, 'rb')
			rep_pkl_data = cPickle.load(pkl_data)
			
			distance = img_rep - rep_pkl_data
			distance = format(np.dot(distance, distance))
			rep_result_list[name[0]] = distance
	
	result_rep_list = list(rep_result_list.values())
	min_result = min(result_rep_list)
	print min_result
	
	for x in rep_result_list:
		temp = rep_result_list[x]
		if temp == min_result:
			id_identifyied = x

	return id_identifyied