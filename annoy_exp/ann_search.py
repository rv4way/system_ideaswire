import os
import numpy as np
import pandas as pd
import cPickle
import compare
from annoy import AnnoyIndex


def search_img(img_path):

	rep_result_list = {}
	temp_rep_list_temp = []

	response =[]

	search_rep = compare.getRep(img_path)
	search_rep_test = list(search_rep)
	#print search_rep_test
	
	#temp_search_rep = np.asarray(search_rep)
	#temp_search_rep = search_rep*1000
	#temp_search_rep = search_rep.astype(np.int32)
	#temp_search_rep = abs(search_rep)
		

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
		n = t.get_nns_by_vector(search_rep_test, 1, -1, True)
		index = n[0][0]

		raw_rep = open(pkl_file, 'rb')
		rep_list = cPickle.load(raw_rep)
		rep = rep_list[index-1]
		#print rep
		#rep = np.asarray(rep)
		rep = list(rep)

		distance = search_rep - rep
		distance = format(np.dot(distance, distance))
		#print distance

		rep_result_list[str(profile_id)] = distance
		temp_rep_list_temp.append(distance)
		#print rep_result

	result_rep_list = list(rep_result_list.values())
	min_result = min(result_rep_list)

	'''sorting distance'''
	temp_rep_list_temp.sort()
	#print temp_rep_list_temp
	#print rep_result_list

	for x in rep_result_list:
		temp = rep_result_list[x]

		if temp == temp_rep_list_temp[0]:
			#print 'top 1', x, temp
			id_identifyied_1 = x
		if temp == temp_rep_list_temp[1]:
			#print 'TOP 2', x, temp
			id_identifyied_2 = x

	top1_dist = float(temp_rep_list_temp[0])
	top2_dist = float(temp_rep_list_temp[1])
	#print top1_dist
	#print top2_dist

	'''now generating response'''


	if top1_dist < float(0.2) or top1_dist == float(0.2):
		response.append(id_identifyied_1)
	elif top1_dist > float(0.7):
		#print response
		return response
	else:
		div_dist = top2_dist/top1_dist
		#print div_dist
		if div_dist < float(1.7):
			response.append(id_identifyied_1)
			response.append(id_identifyied_2)
		elif top1_dist < float(0.5):
			response.append(id_identifyied_1)

	#print response, top1_dist, top2_dist
	#return response, top1_dist, top2_dist
	#print response
	return response

if __name__ == '__main__':
	img_path = '../abhi_05.jpg'
	search_img(img_path)