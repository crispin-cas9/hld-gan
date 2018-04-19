# transform the data

from PIL import Image
import os
import numpy
import pickle

datafolder = os.listdir(path='data')

# def toarray(path):

imlist = []
for file in datafolder:
	if file.endswith('.png'):
		name = "data/" + file
		im = Image.open(name)
		new = im.resize((28, 28))
		new = new.convert("RGB")
		new.save(name)

# return imlist

# datalist = toarray(datafolder)

# output = open('data.pkl', 'wb')
# pickle.dump(datalist, output)
# pklfile = open('data.pkl', 'rb')