from keras.models import Sequential
from keras.layers import Dense

try:

    model_type_Sequential = Sequential()
    model_type_Sequential.add( Dense(
        32,
        activation='relu',
        input_shape = ( num_input_features, )
    ) )
    model_type_Sequential.add( Dense(
        32,
        activation = 'relu'
    ) )
    model_type_Sequential.add( Dense(
       1,
       activation = 'sigmoid'
    ) )
    model_type_Sequential.compile(
        optimizer = 'rmsprop',
        loss= 'binary_crossentropy'
    )
except Exception:
    print( "1. This is for the binary classification task, with the target/labels/output(s) being either 0 or 1\n" )


try:
    model_type_Sequential = Sequential()
    model_type_Sequential.add( Dense(
        32,
        activation = 'relu',
        input_shape = ( num_input_features, )
    ) )
    model_type_Sequential.add( Dense(
        32,
        activation = 'relu',
    ) )
    model_type_Sequential.add( Dense(
        num_classes,
        activation = 'softmax'
    ) )
    model_type_Sequential.compile(
        optimizer = 'rmsprop',
        loss = 'categorical_crossentropy'
    )
except Exception:
    print( "2. This is for single label categorical classification, where the output for each sample is exactly ONE class ie apple\n" )

try:
    model_type_Sequential = Sequential()
    model_type_Sequential.add( Dense(
        32,
        activation = 'relu',
        input_shape = ( num_input_features, )
    ) )
    model_type_Sequential.add( Dense(
        32,
        activation = 'relu'
    ) )
    model_type_Sequential.add( Dense(
        num_classes,
        activation = 'sigmoid'
    ) )
    model_type_Sequential(
        optimizer = 'rmsprop',
        loss = 'binary_crossentropy'
    )
except Exception:
    print( "3. This is for multilabel categorical classification, where each sample can have many outputs ie sample is small, is blue and is also rectangular." )
    print( "Also, please note that the targets/outputs/labels need to be k-hot encoded\n" )


try:
    model_type_Sequential = Sequential()
    model_type_Sequential.add( Dense(
        32,
        activation = 'relu',
        input_shape = ( num_input_features, )
    ) )
    model_type_Sequential.add( Dense(
        32,
        activation = 'relu'
    ) )
    model_type_Sequential.add( Dense(
        num_values_one_or_more,
        activation = None
    ) )
    model_type_Sequential.compile(
        optimizer = 'rmsprop',
        loss = 'mse'
    )
except Exception:
    print( "4. This is for performing regression where the output(s) is a single number or a list of numbers (num_values_one_or_more) " )
    print( "Regarding loss functions commonly used ones are MSE (mean squared error) and MAE (mean absolute error) \n")

try:
    from keras.layers import SeparableConv2D, MaxPooling2D, GlobalAveragePooling2D
    model_type_Sequential = Sequential()
    model_type_Sequential.add( SeparableConv2D(
        32,
        3,
        activation = 'relu',
        input_shape = (
            height,
            width,
            channels
        )
    ) )
    model_type_Sequential.add( SeparableConv2D(
        64,
        3,
        activation = 'relu'
    ) )
    model_type_Sequential.add( MaxPooling2D( 2 ) )
    model_type_Sequential.add( SeparableConv2D(
        64,
        3,
        activation = 'relu'
    ) )
    model_type_Sequential.add( SeparableConv2D(
        128,
        3,
        activation = 'relu'
    ) )
    model_type_Sequential.add( MaxPooling2D( 2 ) )
    model_type_Sequential.add( SeparableConv2D(
        64,
        3,
        activation = 'relu'
    ) )
    model_type_Sequential.add( SeparableConv2D(
        128,
        3,
        activation = 'relu'
    ) )
    model_type_Sequential.add( GlobalAveragePooling2D() )
    model_type_Sequential.add( Dense(
        32,
        activation = 'relu'
    ) )
    model_type_Sequential.add( Dense(
       num_classes,
       activation = 'softmax'
    ) )
    model_type_Sequential.compile(
        optimier = 'rmsprop',
        loss = 'categorical_crossentropy'
    )
except Exception:
    print( "5. This is for single label classification of an image, where the output for each image, as an example. is exactly ONE class ie apple\n" )

try:
    from keras.layers import LSTM

    model_type_Sequential = Sequential()
    model_type_Sequential.add( LSTM(
      32,
      input_shape = ( num_timesteps, num_features )
    ) )
    model_type_Sequential.add( Dense(
        num_classes,
        activation = 'sigmoid'
    ) )
    model_type_Sequential.compile(
        optimizer = 'rmsprop',
        loss = 'binary_crossentropy'
    )
except Exception:
    print( "6. This is a single RNN (Recurrent Neural Network) layer to output either a 0 or 1 to a vector sequence(s)\n" )

try:
    from keras.layers import LSTM
    model_type_Sequential = Sequential()
    model_type_Sequential.add( LSTM(
        32,
        return_sequences = True,
        input_shape = ( num_timesteps, num_features )
    ) )
    model_type_Sequential.add( LSTM(
        32,
        return_sequences = True
    ) )
    model_type_Sequential.add( LSTM( 32 ) )
    model_type_Sequential.add( Dense(
        num_classes,
        activation = 'sigmoid'
    ) )
    model_type_Sequential.compile(
        optimizer = 'rmsprop',
        loss = 'binary_crossentropy'
    )
except Exception:
    print( "7. This is a stacked RNN (Recurrent Neural Network) layer to output either a 0 or 1 to a vector sequence(s)\n" )
