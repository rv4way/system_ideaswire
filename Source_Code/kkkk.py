import os
import search_img
import cv2

tot_count = 0
cor_count = 0
root = '../data/test'
temp = os.listdir(root)
for x in range(len(temp)):
	class_path = os.path.join(root, temp[x])
	img_list = os.listdir(class_path)
	for y in range(len(img_list)):
		img_path = os.path.join(class_path, img_list[y])
		try:
			response = search_img.search_img(img_path)
			tot_count +=1

			k = img_list[y].split('.')
			k = k[0]
			k = k.split('_')
			print k[0]

			for king in range(len(response)):
				if k[0] in response[king]:
					cor_count +=1
					pass

			'''
			#print rep_distance,
			#print top_1
			#print top_2
			k = img_list[y].split('.')
			k = k[0]
			if k in top_1:
				result = str('correct')
			else:
				result = str('incorrect')

			print 'RESULT FOR ', img_path
			print 'ORIGINAL CLASS\t', k
			print 'TOP 1 DISTANCE\t', rep_distance[0]
			print 'TOP 1 ID\t', top_1
			print 'TOP 2 DISTANCE\t', rep_distance[1]
			print 'TOP 2 ID\t', top_2
			print '\n\n'
			#print rep_distance
			tete_rep = []
			for z in range(5):
				tete_rep.append(rep_distance[z])
			print tete_rep
			print '\n\n'
			print te_keke

			print '\n\n'
			programPause = raw_input("Press the <ENTER> key to continue...")
			print '\n\n'
			'''
			print response
			#programPause = raw_input("Press the <ENTER> key to continue...")


			'''
			csv_path = '../top1_50.csv'
			csv_data = open(csv_path, 'a')
			line = ',' + ',' + str(k) + ',' + str(top_1) + ',' + str(rep_distance[0]) +',' + ',' + str(top_2) + ',' +  str(rep_distance[1])
			csv_data.write(line)
			csv_data.write('\n')
			csv_data.close()
			'''
	
		except:
			print '****IN EXCEPTION, PLEASE CHECK****'
			pass

	'''
	csv_path = '../top1_50.csv'
	csv_data = open(csv_path, 'a')
	csv_data.write('\n')
	csv_data.write('\n')
	csv_data.close()
	'''
	


print '**********WORK DONE*********'

print '\n\n\n'
print 'TOTAL IMAGES\t', tot_count
print '\n'
print 'CORRECT IDENTIFYIED\t', cor_count
print '\n\n'
