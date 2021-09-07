from keras.datasets import mnist

(train_images_type_ndarray, train_labels_type_ndarray), (test_images_type_ndarray, test_labels_type_ndarray) = mnist.load_data()

# observe that each training image (60K in total), have integer values for the pixels ranging from 0 to 255
# note that 0 represents black I believe and 255 represents white/brightest colour for a given colour channel
print(train_images_type_ndarray.shape)

print(len(train_labels_type_ndarray))

# see the label values, looks to be 0 1 2 3 4 5 6 7 8 or 9
print(train_labels_type_ndarray)

print(test_images_type_ndarray.shape)

print(len(test_labels_type_ndarray))

print(test_labels_type_ndarray)

from keras import models
from keras import layers

network_type_Sequential = models.Sequential()
network_type_Sequential.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network_type_Sequential.add(layers.Dense(10, activation='softmax'))

# understand what uint8 represents I believe its an integer without a sign so no negative integers from 0 to 255

network_type_Sequential.compile(
    optimizer='rmsprop',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# change the train_images ndarray shape from 60K x 28 x 28 to 60K x 784
train_images_type_ndarray = train_images_type_ndarray.reshape( ( 60000, 28 * 28 ))
# ensure that the values in the ndarray ranges from 0 to 1, 0 being equivalent to black I believe and 1 white
train_images_type_ndarray = train_images_type_ndarray.astype('float32') / 255

test_images_type_ndarray = test_images_type_ndarray.reshape( ( 10000, 28 * 28 ))
test_images_type_ndarray = test_images_type_ndarray.astype('float32') / 255

from keras.utils import to_categorical

# convert the labels ie class 9 becomes [0 0 0 0 0 0 0 0 0 1]
train_labels_type_ndarray = to_categorical( train_labels_type_ndarray )
test_labels_type_ndarray = to_categorical( test_labels_type_ndarray )

network_type_Sequential.fit(train_images_type_ndarray, train_labels_type_ndarray, epochs=5, batch_size=128)

test_loss_type_float, test_accuracy_type_float = network_type_Sequential.evaluate( test_images_type_ndarray, test_labels_type_ndarray )
print(f'test_accuracy: {test_accuracy_type_float}')


import numpy as np
x_type_ndarray = np.array( 12 )
print( x_type_ndarray )
print( x_type_ndarray.ndim )

x_type_ndarray = np.array( [ 12, 3, 6, 14 ] )
print( x_type_ndarray )
print( x_type_ndarray.ndim )

x_type_ndarray = np.array( [ [ 5, 78, 2, 34, 0 ],
                [ 6, 79, 3, 35, 1 ],
                [ 7, 80, 4, 36, 2 ] ] )
print( x_type_ndarray.ndim )

x_type_ndarray = np.array( [ [ [ 5, 78, 2, 34, 0 ],
                  [ 6, 79, 3, 35, 1 ],
                  [ 7, 80, 4, 36, 2 ] ],
                [ [ 5, 78, 2, 34, 0 ],
                  [ 6, 79, 3, 35, 1 ],
                  [ 7, 80, 4, 36, 2 ] ],
                [ [ 5, 78, 2, 34, 0 ],
                  [ 6, 79, 3, 35, 1 ],
                  [ 7, 80, 4, 36, 2 ] ] ] )
print( x_type_ndarray.ndim )