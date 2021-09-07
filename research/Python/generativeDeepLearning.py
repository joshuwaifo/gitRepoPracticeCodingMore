# import the necessary libraries or rather the libraries mentioned in the book
import numpy as np
from keras.utils import to_categorical
from keras.datasets import cifar10

# load the cifar10 dataset
(x_train_type_ndarray, y_train_type_ndarray), (x_test_type_ndarray, y_test_type_ndarray) = cifar10.load_data()

# define the number of classes in the dataset I assume
NUM_CLASSES_type_int = 10

# convert the 0-255 values to first a float32 type and then dividing by 255.0 to ensure it is within the range 0-1
x_train_type_ndarray = x_train_type_ndarray.astype('float32') / 255.0
x_test_type_ndarray = x_test_type_ndarray.astype('float32') / 255.0

# convert the labels which look like values 0-9 to be one hot encoded ie 1 becomes [0 1 0 0 0 0 0 0 0 0]
y_train_type_ndarray = to_categorical(y_train_type_ndarray, NUM_CLASSES_type_int)
y_test_type_ndarray = to_categorical(y_test_type_ndarray, NUM_CLASSES_type_int)

# print the 55th image (out of 50 thousand images), row 13, column 14, colour channel 2
print(x_train_type_ndarray[54, 12, 13, 1])

from keras.models import Sequential
from keras.layers import Flatten, Dense

model_type_Sequential = Sequential([
    Dense( 200, activation = 'relu', input_shape = (32, 32, 3) ),
    Flatten(),
    Dense( 150, activation = 'relu' ),
    Dense( 10, activation = 'softmax' )
])

from keras.layers import Input, Flatten, Dense
from keras.models import Model

input_layer_type_KerasTensor = Input( shape = (32, 32, 3) )

x_type_KerasTensor = Flatten()( input_layer_type_KerasTensor )

x_type_KerasTensor = Dense( units = 200, activation = 'relu' )( x_type_KerasTensor )

x_type_KerasTensor = Dense( units = 150, activation = 'relu' )( x_type_KerasTensor )

output_layer_type_KerasTensor = Dense( units = 10, activation = 'softmax' )( x_type_KerasTensor )

model_type_Functional = Model( input_layer_type_KerasTensor, output_layer_type_KerasTensor )


try:
    x = Dense( units = 200 )( x )
    x = Activation( 'relu' )( x )
except NameError:
    print( "The variable x has not been defined yet" )

try:
    x = Dense( units = 200, activation = 'relu' )( x )
except NameError:
    print( "The variable x has not been defined yet" )

from keras.optimizers import Adam

opt_type_Adam = Adam( lr = 0.0005 )
model_type_Functional.compile( loss = 'categorical_crossentropy', optimizer = opt_type_Adam, metrics = ['accuracy'] )