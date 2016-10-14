import os
import compare
import cPickle
import pandas as pd
import numpy as np

def add_image(profile_id, image):

	rep_img = compare.getRep(image)
	rep_pkl_path = '../img_rep/' + str(profile_id) + '.pkl'

	if os.path.isfile(rep_pkl_path):
		temp_list = []
		temp = open(rep_pkl_path)
		temp_rep = cPickle.load(temp)
		temp_list.append(temp_rep)
		temp_list.append(rep_img)

		f = open(rep_pkl_path, 'wb')
		cPickle.dump(temp_list, f, protocol=cPickle.HIGHEST_PROTOCOL)
		f.close()

	else:

		f = open(rep_pkl_path, 'wb')
		cPickle.dump(rep_img, f, protocol=cPickle.HIGHEST_PROTOCOL)
		f.close()
	update_status(profile_id)

	return 'true'

def update_status(profile_id):

	status_path = '../status.csv'
	status_file = pd.read_csv(status_path, sep = ',', header = None)
	status_file = np.asarray(status_file)
	if profile_id in status_file:
		print 'PROFILE ID PRESENT'
		pass
	else:
		temp_status_file = open(status_path, 'a')
		temp_status_file.write(str(profile_id))
		temp_status_file.write('\n')
		temp_status_file.close()
		print 'STATUS UPDATED'