import numpy as np

array = np.array([0.7,3.1,5.5])

array_linspaced = np.linspace(0,10,5)
array_stepsize = np.arange(0,10,2)

array_2D = np.array([[1,2,3,4],[5,6,7,8]])
array_random1 = np.random.randint(0,100,size = (2,3))
array_random2 = np.random.randint(0,100,size = (2,3))

string1 = "cat"
string2 = "fish"
string3 = string1 + string2

array_random3 = np.concatenate((array_random1,array_random2),axis=0)

new_list = [1, 2, 3, 4]*2
array = array*2

np.sum(array_random3,axis=0)
np.cumsum(array_random3, axis=0)

array_dot = np.dot(array,array.T)
var =np.corrcoef(array_random3)

logic = array_random3 > 75
array_random3[logic]=99

from skimage import io
photo = io.imread('data_for_exercises/scout.png')
import matplotlib.pyplot as plt
saved_photo = plt.imshow(photo[:,:,0].T)

threshold_photo = np.where(photo > 75, 255, 0)
saved_photo = plt.imshow(threshold_photo[:,:,0])

array_1D = np.arange(0,12,1)
reshaped_array = (array_1D.reshape(2,6)).T



plt.savefig('Scout_new.png', dpi=300,bbox_inches="tight")
