import os
import compare
import numpy as np
import pandas as pd
import csv
import cPickle

def search_img(image):

	rep_result_list = {}
	temp_rep_list_temp = []

	response = []

	rep_location = '../img_rep'
	rep_file_list = os.listdir(rep_location)
	if rep_file_list == []:
		print 'DATABASE EMPTY'
		return 'DATABASE EMPTY'

	else:

		'''Generating Rep of the image'''
		img_rep = compare.getRep(image)

		for x in range(len(rep_file_list)):

			'''reading rep saved in .pkl file one by one'''
			name = rep_file_list[x]
			name = name.split('.')
			rep_file_path = os.path.join(rep_location, rep_file_list[x])
			#print rep_file_path
			pkl_data = open(rep_file_path, 'rb')
			rep_pkl_data = cPickle.load(pkl_data)
			

			'''calculating distance of both the rep'''
			distance = img_rep - rep_pkl_data
			distance = format(np.dot(distance, distance))

			'''creating key and vaule pair with distance and id of perticular class'''
			rep_result_list[name[0]] = distance

			'''creating a temp list of distance only'''
			temp_rep_list_temp.append(distance)

	'''getting all the valuse from dictonry of distance and id'''
	result_rep_list = list(rep_result_list.values())
	min_result = min(result_rep_list)

	'''sorting distance'''
	temp_rep_list_temp.sort()
	#print temp_rep_list_temp
	#print rep_result_list

	for x in rep_result_list:
		temp = rep_result_list[x]

		if temp == temp_rep_list_temp[0]:
			print 'top 1', x
			id_identifyied_1 = x
		if temp == temp_rep_list_temp[1]:
			print 'TOP 2', x
			id_identifyied_2 = x

	top1_dist = float(temp_rep_list_temp[0])
	top2_dist = float(temp_rep_list_temp[1])
	print top1_dist
	print top2_dist

	'''now generating response'''


	if top1_dist < float(0.2) or top1_dist == float(0.2):
		response.append(id_identifyied_1)
	elif top1_dist > float(0.6):
		print response
		return response
	else:
		div_dist = top2_dist/top1_dist
		print div_dist
		if div_dist < float(1.7):
			response.append(id_identifyied_1)
			response.append(id_identifyied_2)
		elif top1_dist < float(0.5):
			response.append(id_identifyied_1)

	print response
	return response