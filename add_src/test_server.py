from flask import Flask,jsonify,Response,request, redirect, url_for
import json
from celery import Celery
from celery.utils.log import get_task_logger
from werkzeug.contrib.fixers import ProxyFix
import os
from werkzeug.utils import secure_filename
import cv2
import io
import numpy as np
import pandas as pd
import add_single
import search_img
import time
import check_status


#logger = get_task_logger(__name__)
app = Flask(__name__)
app.config['DEBUG'] = True


'''
app.config['UPLOAD_FOLDER'] = 'uploads/'


app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
celery = Celery(app.name, backend=app.config['CELERY_RESULT_BACKEND'],broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def cel_task():
	logger.info('starting function %s'%(name))

'''

@app.route("/image-processing/face/add",methods=['GET','POST'])
def add_single_iamge():

	try:
		if request.method == 'POST':
			
			header_req = request.headers.get('x-image-profile-id')
			photo = request.files['photo']
			in_memory_file = io.BytesIO()
			photo.save(in_memory_file)
			data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
			color_image_flag = 1
			img = cv2.imdecode(data, color_image_flag)
			temp_path = '../data/add_image/' + str(header_req)+ '.jpg'
			cv2.imwrite(temp_path, img)
			print header_req
			print temp_path
			add_response = add_single.add_image(header_req, temp_path)
			print add_response

			ret_val={'message':'image queued for adding.','status':2,'data':header_req }
			return 	jsonify(**ret_val)

	except:
		ret_val={'message':'request cannot be processed','status':0,'data':header_req }
		return 	jsonify(**ret_val)

@app.route("/image-processing/search", methods = ['GET', 'POST'])
def search_image():
	try:
		if request.method == 'POST':
			
			photo = request.files['photo']
			in_memory_file = io.BytesIO()
			photo.save(in_memory_file)
			data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
			color_image_flag = 1
			img = cv2.imdecode(data, color_image_flag)
			cur_time = time.ctime()
			temp_path = '../data/search_image/' + str(cur_time)+ '.jpg'
			cv2.imwrite(temp_path, img)
			print temp_path

			search_response = search_img.search_img(temp_path)

			if len(search_response) != 0:
				search_response = json.dumps(search_response)
				ret_val={'message':'images found','status': 1,'data': search_response}
				return 	jsonify(**ret_val)
			else:
				search_response = json.dumps(search_response)
				ret_val={'message':'images not found','status':0,'data':search_response}
				return 	jsonify(**ret_val)

	except:
		ret_val={'message':'server error','status':0,'data':'No Data' }
		return 	jsonify(**ret_val)

@app.route("/image-processing/face/status", methods = ['GET', 'POST'])
def status_face():

	try:
		if request.method == 'POST':

			find_status = request.headers.get('x-image-profile-id')
			print find_status
			temp_status = check_status.status(find_status)
			print temp_status

			if temp_status is not None:
				ret_val={'message':'image is added.','status':1,'data': find_status}
				return 	jsonify(**ret_val)
			else:
				ret_val={'message':'image not added.','status':0,'data': find_status}
				return 	jsonify(**ret_val)

	except:
		ret_val={'message':'server error','status':0,'data':header_req }
		return 	jsonify(**ret_val)

if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')