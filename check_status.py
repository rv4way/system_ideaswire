import os
import pandas as pd
import numpy as np

def status(profile_id):
	status_path = '../status.csv'
	status_data = pd.read_csv(status_path, sep = ',', header = None)
	status_data = np.asarray(status_data)
	for x in status_data:
		if x == profile_id:
			return x