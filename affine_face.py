import os
import cv2
import numpy as np
from scipy.misc import imresize
from pylab import array, plot, show, axis, arange, figure, uint8 
import random
from scipy import ndimage
import scipy


def affine_transformation(img, name):
	#img_path = './abhi_05.jpg'
	#img = cv2.imread(img_path)

	#img = imresize(img, (47*5, 55*5))

	#cv2.imshow('ORIGINAL', img)
	#cv2.waitKey()

	rows,cols,ch = img.shape

	#pts1 = np.float32([[50,50],[200,50],[50,200]])
	#pts2 = np.float32([[10,100],[200,50],[100,250]])
	x_rot = 50
	y_rot = 200
	for x in range(2):
		pts1 = np.float32([[50,50],[200,50],[50,200]])

		x_rot = x_rot + 10
		y_rot = y_rot + 10

		pts2 = np.float32([[x_rot, x_rot],[200,50],[x_rot,y_rot]])
	
		M = cv2.getAffineTransform(pts1,pts2)

		dst = cv2.warpAffine(img,M,(cols,rows))
	

		#cv2.imshow('AFFINE', dst)
		#cv2.waitKey()
		cv2.imwrite('./temp/' + str(name) + '_' + str('affine_+_') + str(x_rot) + '_' + str(x) + '.jpg', dst)

	x_rot = 50
	y_rot = 200
	for x in range(2):
		pts1 = np.float32([[50,50],[200,50],[50,200]])

		x_rot = x_rot - 20
		y_rot = y_rot - 20

		pts2 = np.float32([[x_rot, x_rot],[200,50],[x_rot,y_rot]])
	
		M = cv2.getAffineTransform(pts1,pts2)

		dst = cv2.warpAffine(img,M,(cols,rows))
	

		#cv2.imshow(str(('AFFINE', x)), dst)
		#cv2.waitKey()
		cv2.imwrite('./temp/' + str(name) + '_' + str('affine_-_') + str(x_rot) + '_' + str(x) + '.jpg', dst)


def linear_transformation(img_path):
	#img_path = './abhi_05.jpg'
	image = cv2.imread(img_path)

	image = imresize(image, (47*5, 55*5))

	cv2.imshow('original', image)
	cv2.waitKey()

	rows,cols,ch = image.shape

	maxIntensity = 255.0
	x = arange(maxIntensity)


	count = 0
	pair_list = []
	for x in range(15):

		val_list = [0.9, 1.0, 1.1]

		phi = random.choice(val_list)
		theta = random.choice(val_list)
		#print phi, theta

		pair = str((phi, theta))
		#pair_list.append(pair)

		if pair in pair_list:
			print 'GOOD'
		else:
			pair_list.append(pair)

			newImage0 = (maxIntensity/phi)*(image/(maxIntensity/theta))**0.5
			newImage0 = array(newImage0,dtype=uint8)

			name = str(pair) + '_' + str('img_0') + '_' + str(x)
			affine_transformation(newImage0, name)

			#cv2.imshow(str((phi, theta)),affine_newImage0)
			#cv2.waitKey()
			cv2.imwrite('./temp/' + str(name) + '_original_0_' + str(x) + '.jpg', newImage0)

			newImage1 = (maxIntensity/phi)*(image/(maxIntensity/theta))**2
			newImage1 = array(newImage1,dtype=uint8)

			name = str(pair) + '_' + str('img_1') + '_' + str(x)
			affine_transformation(newImage1, name)

			#cv2.imshow(str((phi, theta)),newImage1)
			#cv2.waitKey()
			cv2.imwrite('./temp/' + str(name) + '_original_1_' + str(x) + '.jpg', newImage1)

	print 'PAIR LIST', pair_list


'''
def distance_transformation(img_path):

	image = cv2.imread(img_path)

	image = imresize(image, (47*5, 55*5))

	cv2.imshow('original', image)
	cv2.waitKey()

	rows,cols,ch = image.shape

	img = np.array(image)

	#A = np.matrix([[1,3,7],[2,8,3],[7,8,1]])
	#A = np.linalg.matrix_rank(img)

	indices = np.zeros(((np.ndim(img),) + img.shape), dtype=np.int32)
	
	#img = ndimage.distance_transform_edt(img, sampling=A)
	img = ndimage.distance_transform_edt(img, return_indices=True, indices=indices)

	cv2.imshow('distance_transformation', img)
	cv2.waitKey()
'''



if __name__ == '__main__':

	img_path = './subham_06.jpg'
	linear_transformation(img_path)
	