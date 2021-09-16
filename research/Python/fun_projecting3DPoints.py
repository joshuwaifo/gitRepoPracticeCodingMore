from scipy.linalg import expm, rq, det, inv
from numpy import dot, loadtxt, vstack, ones, hstack, eye, array, diag, sign
from matplotlib.pyplot import figure, plot, show
from numpy.random import rand

class Camera( object ):
    """ Class for representing pin-hole cameras. """

    def __init__( self, P ):
        """ Initialize P = K[R|t] camera model. """
        self.P = P
        self.K = None # calibration matrix
        self.R = None # rotation
        self.t = None # translation
        self.c = None # camera center

    def project( self, X ):
        """ Project points in X (4*n array) and normalize coordinates. """
        x = dot(
            self.P,
            X
        )

        for i in range( 3 ):
            x[ i ] /= x[ 2 ]

        return x

    def rotation_matrix( a ):
        """ Creates a 3D rotation matrix for rotation
        around the axis of the vector a. """
        R = eye( 4 )
        R[ :3, :3 ] = expm( [
            [ 0, -a[ 2 ], a[ 1 ] ],
            [ a[ 2 ], 0, -a[ 0 ] ],
            [ -a[ 1 ], a[ 0 ], 0 ]
        ] )
        return R

    def factor( self ):
        """ Factorize the camera matrix into K, R, t as P = K[R|t]. """

        # factor first 3*3 part
        K, R = rq( self.P[ :, :3 ] )

        # make diagonal of K positive
        T = diag( sign( diag( K ) ) )
        if  det( T ) < 0:
            T[ 1, 1 ] *= -1

        self.K = dot( K, T )
        self.R = dot( T, R ) # T is its own inverse
        self.t = dot(
            inv( self.K ),
            self.P[ :, :3 ]
        )

        return self.K, self.R, self.t

    def center( self ):
        """ Compute and return the camera center. """

        if self.c is not None:
            return self.c
        else:
            # compute c by factoring
            self.K, self.R, self.t = self.factor()
            self.c = -dot(
                self.R.T,
                self.T
            )
            return self.c
try:
    import camera
    points = loadtxt('house.p3d').T
    points = vstack( (
        points,
        ones( points.shape[1] )
    ) )

    # setup camera
    P = hstack( (
        eye( 3 ),
        array(
            [
                [0],
                [0],
                [-10]
            ]
        )
    ) )
    cam = camera.Camera( P )
    x = cam.project( points )

    # plot projection
    figure()
    plot(
        x[ 0 ],
        x[ 1 ],
        'k.'
    )
    show()

    # create transformation
    r = 0.05 * rand( 3 )
    rot = camera.rotation_matrix( r )

    # rotate camera and project
    figure()
    for t in range( 20 ):
        cam.P = dot(
            cam.P,
            rot
        )
        x = cam.project( points )
        plot(
            x[ 0 ],
            x[ 1 ],
            'k.'
        )
    show()


    import camera

    K = array(
        [
            [ 1000, 0, 500 ],
            [ 0, 1000, 300 ],
            [ 0, 0, 1 ]
        ]
    )
    tmp = camera.rotation_matrix( [ 0, 0, 1 ] )[ :3, :3 ]
    Rt = hstack( (
        tmp,
        array(
            [
                [ 50 ],
                [ 40 ],
                [ 30 ]
            ]
        )
    ) )

    cam = camera.Camera( dot(
        K,
        Rt
    ) )

    print(K, Rt)
    print(cam.factor())

except Exception:
    print("Hopefully debug and figure out with time, if not, it's okay")
