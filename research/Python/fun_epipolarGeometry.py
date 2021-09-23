try:
    import camera
    from numpy import array, loadtxt, genfromtxt, vstack, ones
    from PIL import Image
    from matplotlib.pyplot import figure, imshow, plot, axis, show

    # load some images
    im1 = array( Image.open( 'images/001.jpg' ) )
    im2 = array( Image.open( 'images/002.jpg' ) )

    # load 2D points for each view to a list
    points2D =  [
        loadtxt( '2D/00' + str( i+1 ) + '.corners' ).T for i in range( 3 )
    ]

    # load 3D points
    points3D = loadtxt( '3D/p3d' ).T

    # load correspondences
    corr = genfromtxt(
        '2D/nview-corners',
        dtype = 'int',
        missing = '*'
    )

    # load cameras to a list of Camera objects
    P = [
        camera.Camera( loadtxt( '2D/00' + str( i+1 ) + '.P' ) ) for i in range( 3 )
    ]

    exec( open( 'load_vggdata.py' ) ).read()

    # make 3D points homogeneous and project
    X = vstack(
        (
            points3D,
            ones( points3D.shape[ 1 ] )
        )
    )

    x = P[0].project(X)

    # plotting the points in view 1
    figure()
    imshow( im1 )
    plot(
        x[ 0 ],
        x[ 1 ],
        'r.'
    )
    axis( 'off' )

    show()
except Exception:
    print("Sort out the errors later")

from matplotlib.pyplot import figure, show
from mpl_toolkits.mplot3d import axes3d

fig_type_Figure = figure()
ax_type_Axes3DSubplot = fig_type_Figure.gca( projection = "3d" )

# generate 3D sample data
X_type_ndarray, Y_type_ndarray, Z_type_ndarray = axes3d.get_test_data( 0.5 )

# plot the points in 3D
ax_type_Axes3DSubplot.plot(
    X_type_ndarray.flatten(),
    Y_type_ndarray.flatten(),
    Z_type_ndarray.flatten(),
    'o'
)

show()

try:
    # plotting 3D points
    from mpl_toolkits.mplot3d import axes3d
    from matplotlib.pyplot import figure

    fig = figure()
    ax = fig.gca( projection = "3d" )
    ax.plot(
        points3D[ 0 ],
        points3D[ 1 ],
        points3D[ 2 ],
        'k.'
    )

except Exception:
    print( "Need to get the data for points3D from the first try-except block" )

from numpy import zeros
from scipy.linalg import svd
def compute_fundamental( x1, x2 ):
    """ Computes the fundamental matrix from corresponding points
        (x1, x2, 3*n arrays) using the normalized 8 point algorithm.
        each row is constructed as
        [ x' * x, x' * y, x' * z, y' * x, y' * y, y' * z, z' * x, z' * y, z'* z ] """

    n = x1.shape[ 1 ]
    if x2.shape[ 1 ] != n:
        raise ValueError( "Number of points don't match." )

    # build matrix for equations
    A = zeros( ( n, 9 ) )
    for i in range( n ):
        A[ i ] = [
            x1[ 0, i ] * x2[ 0, i ],
            x1[ 0, i ] * x2[ 1, i ],
            x1[ 0, i ] * x2[ 2, i ],
            x1[ 1, i ] * x2[ 0, i ],
            x1[ 1, i ] * x2[ 1, i ],
            x1[ 1, i ] * x2[ 2, i ],
            x1[ 2, i ] * x2[ 0, i ],
            x1[ 2, i ] * x2[ 1, i ],
            x1[ 2, i ] * x2[ 2, i ]

        ]

    # compute linear least square solution
    U, S, V = svd( A )
    F = V[ -1 ].reshape( 3, 3)