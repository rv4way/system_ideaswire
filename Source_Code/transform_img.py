import os
import cv2
import numpy as np
import pandas as pd
from scipy.misc import imresize
#from pylab import array, plot, show, axis, arange, figure, uint8 
import random
from scipy import ndimage
import scipy
import compare
import cPickle
import update_annoy as ann

def transform_image(img_path, profile_id):

	profile_path = os.path.join('../data/add_image', str(profile_id))
	if not os.path.exists(profile_path):
		os.mkdir(profile_path)
	
	img = cv2.imread(img_path)
	img = imresize(img, (47*5, 55*5))

	pair_list = []
	for k in range(45):
		alpha_list = [1.0, 1.5, 2.0, 2.5, 3.0]
		beta_list = [x for x in range(20, 100, 10)]

		alpha = random.choice(alpha_list)
		beta = random.choice(beta_list)
		
		pair = str((alpha, beta))

		if pair in pair_list:
			pass
		else:
			pair_list.append(pair)

			name = str(profile_id) + pair + '_' + str(k)

			mul_img = cv2.multiply(img,np.array([alpha]))
			new_img = cv2.add(mul_img, beta)

			con_img = convolve_image(new_img)

			save_path = profile_path + '/' + name + '.jpg'
			cv2.imwrite(save_path, con_img)
	return profile_path


def convolve_image(img):

	kernel = np.array([ [0,-1,0],
                    [-1,5,-1],
                    [0,-1,0] ],np.float32)

	new_img = cv2.filter2D(img,-1,kernel)
	return new_img

def cal_rep(profile_path, profile_id):
	#print profile_id
	image_list = os.listdir(profile_path)
	for x, y in enumerate(image_list):
		img_path = os.path.join(profile_path, y)
		img_rep = compare.getRep(img_path)
		store_rep(img_rep, profile_id)
	print 'REP WRITTEN TO DISK'

def store_rep(img_rep, profile_id):

	rep_location = '../img_rep'
	rep_file = os.path.join(rep_location, str(profile_id)) + '.pkl'
	img_rep = list(img_rep)
	
	if os.path.isfile(rep_file):
		temp_list = []
		temp = open(rep_file)
		temp_rep = cPickle.load(temp)
		#print len(temp_rep)
		for x in range(len(temp_rep)):
			temp_list.append(temp_rep[x])
		
		temp_list.append(img_rep)

		f = open(rep_file, 'wb')
		cPickle.dump(temp_list, f, protocol=cPickle.HIGHEST_PROTOCOL)
		f.close()
	
	else:
		f = open(rep_file, 'wb')
		cPickle.dump([img_rep], f, protocol=cPickle.HIGHEST_PROTOCOL)
		f.close()
	update_status(profile_id)


def update_status(profile_id):

	'''updating status file of the id'''
	status_path = '../status.csv'
	status_file = pd.read_csv(status_path, sep = ',', header = None)
	status_file = np.asarray(status_file)
	if profile_id in status_file:
		pass
	else:
		temp_status_file = open(status_path, 'a')
		temp_status_file.write(str(profile_id))
		temp_status_file.write('\n')
		temp_status_file.close()
		print 'STATUS UPDATED'
	

def main_fun(img_path, profile_id):
	profile_path = transform_image(img_path, profile_id)
	#profile_path = os.path.join('../data/add_image', str(profile_id))
	cal_rep(profile_path, profile_id)
	ann.create_annoy(profile_id)



if __name__ == '__main__':
	img_path = '../nisha_03.jpg'
	main_fun(img_path, 'nisha_03')