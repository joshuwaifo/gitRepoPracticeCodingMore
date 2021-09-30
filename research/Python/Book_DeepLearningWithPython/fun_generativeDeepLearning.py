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

for i in range(
        0,
        len( text_type_str )-maxlen_type_int,
        step_type_int
):
    sentences_type_list.append( text_type_str[ i: i + maxlen_type_int ] )
    next_chars_type_list.append( text_type_str[ i + maxlen_type_int ] )

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
y = np.zeros(
    (
        len( sentences_type_list ),
        len( chars_type_list )
    ),
    dtype = bool
)

for i, sentence_type_str in enumerate( sentences_type_list ):
    for t, char_type_str in enumerate( sentence_type_str ):
        x[
            i,
            t,
            char_indices_type_dict[ char_type_str ]
        ] = 1
        y[
            i,
            char_indices_type_dict[ next_chars_type_list[ i ] ]
        ] = 1