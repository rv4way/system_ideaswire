import os
import shutil

root_dir = '/media/rahul/42d36b39-1ad7-45d4-86bb-bf4e0a66a97f/Data Sets/Celeb Dataset/aligned_images_DB'
dest_path = '/media/rahul/42d36b39-1ad7-45d4-86bb-bf4e0a66a97f/ideaswire_openface_src/data/image'
test_path = '/media/rahul/42d36b39-1ad7-45d4-86bb-bf4e0a66a97f/ideaswire_openface_src/data/test'
in_root = os.listdir(root_dir)
for x in range(100):#len(in_root)):
	celeb = os.path.join(root_dir, in_root[x])
	in_cele = os.listdir(celeb)
	for y in range(len(in_cele)):
		in_cele_path = os.path.join(celeb, in_cele[y])
		img_list = os.listdir(in_cele_path)
		a = 0
		for z in range(15):#len(img_list)):
			'''
			img_path = os.path.join(in_cele_path, img_list[z])
			new_dest = os.path.join(dest_path, in_root[x])
			if not os.path.exists(new_dest):
				os.mkdir(new_dest)
			shutil.copy(img_path, new_dest+'/')
			'''
			if a < 10:
				img_path = os.path.join(in_cele_path, img_list[a])
				a += 1
				new_dest = os.path.join(dest_path, in_root[x])
				if not os.path.exists(new_dest):
					os.mkdir(new_dest)
				shutil.copy(img_path, new_dest+'/')

			else:
				img_path = os.path.join(in_cele_path, img_list[a])
				a += 1
				new_dest = os.path.join(test_path, in_root[x])
				if not os.path.exists(new_dest):
					os.mkdir(new_dest)
				shutil.copy(img_path, new_dest+'/')
	print 'DONE FOR', in_root[x]