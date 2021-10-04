# SECTION 1: TEXT GENERATION WITH an LSTM

import numpy as np
def reweight_distribution( original_distribution, temperature = 0.5 ):
    distribution = np.log( original_distribution ) / temperature
    distribution = np.exp(distribution)
    return distribution / np.sum( distribution )


import keras
import numpy as np
path_type_str = keras.utils.get_file(
    'nietzsche.txt',
    origin = 'https://s3.amazonaws.com/text-datasets/nietzsche.txt'
)
text_type_str = open( path_type_str ).read().lower()
print( f"Corpus length: { len( text_type_str ) }" )


maxlen_type_int = 60
step_type_int = 3
sentences_type_list = []
next_chars_type_list = []

for i_type_int in range(
        0,
        len( text_type_str )-maxlen_type_int,
        step_type_int
):
    sentences_type_list.append( text_type_str[ i_type_int: i_type_int + maxlen_type_int ] )
    next_chars_type_list.append( text_type_str[ i_type_int + maxlen_type_int ] )

print( f"Number of sequences: { len( sentences_type_list ) }" )

# observe that this seems like a really useful function to get just the unique characters in long text
# especially set( pieceoftextLikeABook )
chars_type_list = sorted( list( set( text_type_str ) ) )
print( f"Unique characters: { len( chars_type_list ) }" )

char_indices_type_dict = dict(
    (
        char_type_str,
        chars_type_list.index( char_type_str )
    )
    for char_type_str in chars_type_list
)

print( "Vectorization..." )

x = np.zeros(
    (
        len( sentences_type_list ),
        maxlen_type_int,
        len( chars_type_list )
    ),
    dtype = bool
)
y = np.zeros(1
    (
        len( sentences_type_list ),
        len( chars_type_list )
    ),
    dtype = bool
)

for i_type_int, sentence_type_str in enumerate( sentences_type_list ):
    for t_type_int, char_type_str in enumerate( sentence_type_str ):
        x[
            i_type_int,
            t_type_int,
            char_indices_type_dict[ char_type_str ]
        ] = 1
        y[
            i_type_int,
            char_indices_type_dict[ next_chars_type_list[ i_type_int ] ]
        ] = 1

try:
    from keras.layers import LSTM, Dense
    from keras.models import Sequential
    from keras.optimizers import RMSprop

    model_type_Sequential = Sequential()
    model_type_Sequential.add( LSTM(
        128,
        input_shape = (
            maxlen_type_int,
            len( chars_type_list )
        )
    ) )

    model_type_Sequential.add( Dense(
        len( chars_type_list ),
        activation = 'softmax'
    ) )

    optimizer = RMSprop( lr = 0.01 )
    model_type_Sequential.compile(
        loss = 'categorical_crossentropy',
        optimizer = optimizer
    )
except Exception:
    print( "The LSTM layer is not working for some reason" )

def sample(
        preds,
        temperature = 1.0
):
    preds = np.asarray( preds ).astype( 'float64' )
    preds = np.log( preds ) / temperature
    exp_preds = np.exp( preds )
    preds = exp_preds / np.sum( exp_preds )
    probas = np.random.multinomial(
        1,
        preds,
        1
    )
    return np.argmax( probas )

import random
import sys

for epoch in range(
        1,
        60
):
    print( f"epoch: {epoch}" )

    model_type_Sequential.fit(
        x,
        y,
        batch_size = 128,
        epochs = 1
    )

    start_index = random.randint(
        0,
        len( text_type_str ) - maxlen_type_int - 1
    )

    generated_text = text_type_str[ start_index : start_index + maxlen_type_int ]
    print( f"--- Generating with seed: { generated_text } " )

    for temperature in [
        0.2,
        0.5,
        1.0,
        1.2
    ]:

        print( f"------ temperature: { temperature }" )
        sys.stdout.write( generated_text )

        for i in range( 400 ):

            sampled = np.zeros( (
                1,
                maxlen_type_int,
                len( chars_type_list )
            ) )

            for t, char in enumerate( generated_text ):

                sampled[
                    0,
                    t,
                    char_indices_type_dict[ char ]
                ] = 1

            preds = model_type_Sequential.predict(
                sampled,
                verbose = 0
            )[ 0 ]

            next_index = sample(
                preds,
                temperature
            )

            next_char = chars_type_list[ next_index ]

            generated_text += next_char
            generated_text = generated_text[ 1 : ]

            sys.stdout.write( next_char )