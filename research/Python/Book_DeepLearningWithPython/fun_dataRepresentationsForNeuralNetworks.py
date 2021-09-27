from keras.datasets import mnist

# load 4 numpy arrays (training data and corresponding labels) and (testing data and corresponding labels)
( train_images_type_ndarray, train_labels_type_ndarray ), ( test_images_type_ndarray, test_labels_type_ndarray ) = mnist.load_data()

print( train_images_type_ndarray.ndim )

print( train_images_type_ndarray.shape )

print( train_images_type_ndarray.dtype )

# note that uint8 means unsigned integer which means it has no sign so it starts from 0

# get the 5th image in the train_images_type_ndarray numpy array
digit_type_ndarray = train_images_type_ndarray[4]
from matplotlib.pyplot import imshow, cm, show

# set the ground work for the image you want to display in binary (black or white)
imshow(
    digit_type_ndarray,
    cmap = cm.binary
)
# display the processed image output
show()

# get the 11th image up to and including the 99th image
my_slice_type_ndarray = train_images_type_ndarray[ 10 : 100 ]
print( my_slice_type_ndarray.shape )