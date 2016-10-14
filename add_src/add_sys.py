import os
import compare



def add_video():

	class_list = os.listdir('../data/image')
	for x in range(len(class_list)):
		class_name = os.path.join('../data/image', class_list[x])
		img_list = os.listdir(class_name)
		for y in range(10):
			image_path = os.path.join(class_name, img_list[y])
			try:
				temp_rep = compare.getRep(image_path)
				rep_file_path = '../img_rep/' + str(class_list[x]) + '.csv'
				rep_file = open(rep_file_path, 'a')
				for z in temp_rep:
					line = str(z) + ','
					rep_file.write(line)
				rep_file.write('\n')
				rep_file.close()
			except:
				pass
		print 'rep created for', class_list[x]
		
if __name__ == '__main__':
	add_video()