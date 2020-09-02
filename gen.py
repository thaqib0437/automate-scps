from PIL import Image
import numpy as np
import sys
import os
import random 



def gen(d, name): 
	data = np.zeros((d,d, 3), dtype=np.uint8)
	s = random.choice(range(255))
	random.seed(s)
	x = random.choice(range(255))

	s = random.choice(range(255))
	random.seed(s)
	y = random.choice(range(255))

	s = random.choice(range(255))
	random.seed(s) 

	z = random.choice(range(255))
	p = [x,y,z]
	base = [255,255,255]
	data[0:d, 0:d] = base #Filling the full image with base

	block = np.zeros((70,70,3), dtype = np.uint8)
	block[0:70, 0:70] = [x,y,z]
	
	data[35:105, 35:105] = block

		#First ROW:
	for i in range(35,325,70):
		print(i)
		print(i+70)
		for j in range(35,325,70):
			if random.random()>0.3:
				data[i:i+70, j:j+70]=block
        #Reflecting the image
	data[0:420,35:105] = data[0:420,315:385]
	data[0:420, 105:175] = data[0:420, 245:315]
	
	
	img = Image.fromarray(data, 'RGB')
	img.save(name + '.png')
	img.show()




gen(420, 'out1')
print(random.random())
