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