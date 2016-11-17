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

	#calculation rep of the image
	search_rep = compare.getRep(img_path)
	search_rep_test = list(search_rep)
	print search_rep_test
	hjhjhjhjh

	ann_location = '../annoy/face_module.ann'
	pkl_location = '../img_rep'
	label_id = '../annoy/label_id.csv'

	t = AnnoyIndex(128, metric = 'eucledian')
	t.load(ann_location)
	n = t.get_nns_by_vector(search_rep_test, 10, -1, True)
	ann_rep = n[0]
	dis_rep = n[1]


	'''
	top1_dist = float(dis_rep[0])
	top2_dist = float(dis_rep[1])
	#print top1_dist
	#print top2_dist

	label_data = pd.read_csv(label_id, 'rb')
	label_data = np.asarray(label_data)

	id_identifyied_1 = label_data[ann_rep[0]-1]
	id_identifyied_1 = str(id_identifyied_1)
	id_identifyied_1 = id_identifyied_1.split(',')
	id_identifyied_1 = id_identifyied_1[1][:-2]


	id_identifyied_2 = label_data[ann_rep[1]-1]
	id_identifyied_2 = str(id_identifyied_2)
	id_identifyied_2 = id_identifyied_2.split(',')
	id_identifyied_2 = id_identifyied_2[1][:-2]

	#print id_identifyied_1
	#print id_identifyied_2


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
	print response
	return response

	'''
	label_data = pd.read_csv(label_id, 'rb')
	label_data = np.asarray(label_data)
	for x in ann_rep:
		profile_id = label_data[x-1]
		profile_id = str(profile_id)
		profile_id = profile_id.split(',')
		profile_id = profile_id[1][:-2]
		rep_file = os.path.join(pkl_location, (profile_id + '.pkl'))
		rep_data = open(rep_file, 'rb')
		rep_data = cPickle.load(rep_data)
		for k, y in enumerate(rep_data):
			#print y
			distance = search_rep - y
			distance = format(np.dot(distance, distance))
			#print distance

			rep_result_list[str(profile_id)] = distance
			temp_rep_list_temp.append(distance)
	

	result_rep_list = list(rep_result_list.values())
	min_result = min(result_rep_list)


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

	#now generating response


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
	print response
	return response

if __name__ == '__main__':
	img_path = '../upsana_05.jpg'
	search_img(img_path)