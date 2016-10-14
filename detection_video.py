import os
import cv2
import dlib
import sys
#from skimage import io
import numpy as np
#from scipy.misc import imresize


def detection_test():

	img_count = 0
	det_count = 0
	det_flase = 0
	tem2 = 0
	tem1 = 0
	detector = dlib.get_frontal_face_detector()
	root_dir = '/media/rahul/42d36b39-1ad7-45d4-86bb-bf4e0a66a97f/ideaswire_openface_src/data/video'
	dest_path = '/media/rahul/42d36b39-1ad7-45d4-86bb-bf4e0a66a97f/ideaswire_openface_src/data/image'
	name_list = os.listdir(root_dir)
	print len(name_list)
	
	for x in range(len(name_list)):
		count =0
		name_path = os.path.join(root_dir, name_list[x])
		print name_path
		name = name_list[x].split('.')
		print name
		
		#image = cv2.imread(image_path)
	
		cap = cv2.VideoCapture(name_path)
		success, image = cap.read()	
		while success:
			success, image = cap.read()
			if success:
				image = np.rot90(image, 1)
				#cv2.imshow('ROTATION 1', image)
				#cv2.waitKey()
				img_count = img_count + 1
				dets = detector(image, 0)
				if dets:
					det_count = det_count + 1
					#crop_image = face_crop(image, dets)
					crop_image = image
				else:
					image = np.rot90(image, 2)
					#cv2.imshow('ROTAION 2', image)
					#cv2.waitKey()
					img_count = img_count + 1
					dets = detector(image, 0)
					if dets:
						det_count = det_count + 1
						#crop_image = face_crop(image, dets)
						crop_image = image

					else:
						image = np.rot90(image, 3)
						#cv2.imshow('ROTAION 3', image)
						#cv2.waitKey()
						img_count = img_count + 1
						dets = detector(image, 0)
						if dets:
							det_count = det_count + 1
							#crop_image = face_crop(image, dets)
							crop_image = image

						else:
							image = np.rot90(image, 0)
							#cv2.imshow('ROTAION 0', image)
							#cv2.waitKey()
							img_count = img_count + 1
							dets = detector(image, 0)
							if dets:
								det_count = det_count + 1
								#crop_image = face_crop(image, dets)
								crop_image = image



				#dest_new_path = dest_path + '/' + name[0]
				dest_new_path = os.path.join(dest_path, name[0])

				if not os.path.exists(dest_new_path):
					os.mkdir(dest_new_path)
					#dest_make_path = os.path.join(dest_new_path, str(0))
					#os.mkdir(dest_make_path)
				#else:
					#in_dest_list = os.listdir(dest_new_path)
					#last_index = in_dest_list[-1]
					#dest_make_path = os.path.join(dest_new_path, last_index)

				cv2.imwrite(dest_new_path + '/' + name[0] +'_' + str(count) + '.jpg', crop_image)
				print 'image saved', name[0], count
				count = count + 1
				#cv2.imshow('jkjk', crop_image)
				#cv2.waitKey()
	

	print 'total video', x
	print 'total image', img_count
	print 'total face detected', det_count
	print 'total face not detected', det_flase


def face_crop(image, dets):
	for i, d in enumerate(dets):
		left = d.left()
		top = d.top()
		bottom = d.bottom()
		rit = d.right()
		temp = image[top-5:bottom+5, left-5:rit+5]
		try:
			crop_image = imresize(temp, (47,55))
			return crop_image
		except:
			print 'FACE NOT FOUND OR VIDEO ENDED'
			return None

if __name__ == '__main__':
	detection_test()