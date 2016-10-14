
import cv2
import itertools
import os

import numpy as np
np.set_printoptions(precision=2)

import openface


align = openface.AlignDlib('../model/shape_predictor_68_face_landmarks.dat')
net = openface.TorchNeuralNet('../model/nn4.small2.v1.t7')



def getRep(imgPath):

	bgrImg = cv2.imread(imgPath)

	rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

	bb = align.getLargestFaceBoundingBox(rgbImg)

	imgDim = 96
	alignedFace = align.align(imgDim, rgbImg, bb,
                              landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)

	rep = net.forward(alignedFace)

	return rep

'''

if __name__ == '__main__':

	csv_file_path = '/home/rahul/Desktop/openface_result_1.csv'
	root_path = '/media/rahul/42d36b39-1ad7-45d4-86bb-bf4e0a66a97f/new_system/data/test_images/test1'
	in_root = os.listdir(root_path)
	for x in range(len(in_root)):
		imgPath_1 = os.path.join(root_path, in_root[x])
		img_name_1 = in_root[x]
		for y in range(len(in_root)):
			imgPath_2 = os.path.join(root_path, in_root[y])
			img_name_2 = in_root[y]

			#print imgPath_1
			#print imgPath_2
			print img_name_1
			print img_name_2

			distance = getRep(imgPath_1) - getRep(imgPath_2)
			distance = format(np.dot(distance, distance))

			print distance
			
			file_data = open(csv_file_path, 'a')
			line = str(img_name_1) + ',' + str(img_name_2) + ',' + str(distance) + '\n'
			file_data.write(line)
			file_data.close()
'''