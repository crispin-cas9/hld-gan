# transform the data

from PIL import Image
import os
import numpy
import pickle

datafolder = os.listdir(path='data')

def toarray(path):
	imlist = []
	for file in path:
		if file.endswith('.png'):
			im = Image.open("data/" + file)
			new = im.resize((28, 28))
			new = new.convert("RGB")
			imlist.append(numpy.array(new))
	return imlist

datalist = toarray(datafolder)

output = open('data.pkl', 'wb')

pickle.dump(datalist, output)

# pklfile = open('data.pkl', 'rb')
# = pickle.load(pklfile)