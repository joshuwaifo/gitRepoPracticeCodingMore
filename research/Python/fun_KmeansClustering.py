from numpy.random import randn
from numpy import array, vstack, where

from scipy.cluster.vq import kmeans, vq
from matplotlib.pyplot import figure, plot, axis, show

class1_type_ndarray = 1.5 * randn( 100, 2)

class2_type_ndarray = randn( 100, 2) + array(
    [
        5,
        5
    ]
)

# vertical stack (increasing the number of rows for example, from 100 to 200)
features_type_ndarray = vstack(
    (
        class1_type_ndarray,
        class2_type_ndarray
    )
)

centroids_type_ndarray, _ = kmeans( features_type_ndarray, 2)

code_type_ndarray, _ = vq(
    features_type_ndarray,
    centroids_type_ndarray
)

figure()
ndx = where( code_type_ndarray == 0 )[ 0 ]
plot(
    features_type_ndarray[ ndx, 0 ],
    features_type_ndarray[ ndx, 1 ],
    '*'
)
ndx = where( code_type_ndarray == 1 )[ 0 ]
plot(
    features_type_ndarray[ ndx, 0 ],
    features_type_ndarray[ ndx, 1 ],
    'r.'
)
plot(
    centroids_type_ndarray[ :, 0 ],
    centroids_type_ndarray[ :, 1 ],
    'go'
)
axis( 'off' )
show()


try:
    import imtools
    import pickle
    from scipy.cluster.vq import *

    # get list of images
    imlist = imtools.get_imlist( 'selected_fontimages/' )
    imnbr = len( imlist )
except Exception:
    print( "the function imtools.get_imlist is not currently available, will hopefully sort it out later" )

