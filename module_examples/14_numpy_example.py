import numpy as np

my_list = [4,5,6,7]
my_array = np.array([4,5,6,7])
my_array = np.array(my_list)

#we can square each element in the arraty
squared_array = my_array**2



#linear space an array
lin_spaced = np.linspace(0,7,30)

#regularly spacing
reg_spaced = np.arange(0,10.1,2)

#create array and fill with rand integers
rand_array1 = np.random.randint(0, 100, size=(2,3))
rand_array2 = np.random.randint(0, 100, size=(2,3))

combined_arr = np.concatenate([rand_array1,rand_array2],axis=1)
combined_arr = combined_arr-1000



#cool descriptive statistics
sum_arr = np.sum(rand_array1) #will sum entire array
sum_arr_axis1 = np.sum(rand_array1, axis=0)#np.sum(axis=1) will sum along rows
#we have min(), max(), std(), variance(), mean(), cumsum() and more!
#cumsum() adds each row with previous value
cumulative_arr = np.cumsum(rand_array1,axis=0)



exp_ex = np.exp(-5)

#matrix operations
dot = np.dot(rand_array1, rand_array1.T)
arr1_T = rand_array1.T


#logic array 
logic_arr = rand_array1 > 50
# %%


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

# %%

from skimage import io
photo = io.imread('data_for_exercises/scout.png')
import matplotlib.pyplot as plt
#to show the image with normal colors
import matplotlib.image as mpimg
#imread loads the multidimensional numpy array with red, green, blue channels
image = mpimg.imread("data_for_exercises/scout.png")
plt.imshow(image)


#to work with image as an array
import matplotlib.pyplot as plt
plt.imshow(photo)
saved_photo = plt.imshow(photo[:,:,0],cmap='Reds')
#Default color maps is yellow to purple
#saved_photo = plt.imshow(photo[:,:,0])
saved_photo = plt.imshow(photo[:,:,1],cmap='Greens')
saved_photo = plt.imshow(photo[:,:,2],cmap='Blues')


threshold_photo = np.where(photo[:,:,0] > 75, 255, 0)
saved_photo = plt.imshow(threshold_photo[:,200:800,0])

array_1D = np.arange(0,12,1)
reshaped_array = (array_1D.reshape(2,6)).T



plt.savefig('data_for_exercises/Scout_new.png', dpi=300,bbox_inches="tight")
