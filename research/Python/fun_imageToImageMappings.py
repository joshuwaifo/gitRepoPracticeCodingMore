from numpy import vstack, ones, mean, std, diag, dot, zeros, linalg, array, argsort, concatenate
from scipy.ndimage import filters
from matplotlib.pyplot import figure, gray, imshow, plot, axis, show
from PIL import Image
from scipy import ndimage

def normalize(points):
    """ Normalize a collection of points in
    homogeneous coordinates so that last row = 1."""

    for row in points:
        row /= points[-1]

    return points

def make_homog(points):
    """ Convert a set of points (dim*n array) to
    homogeneous coordinates. """
    return vstack((points, ones((1, points.shape[1]))))



def H_from_points(fp, tp):
    """ Find homography H, such that fp is mapped to tp
    using the linear DLT method. Points are conditioned
    automatically. """

    if fp.shape != tp.shape:
        raise RuntimeError('number of points do not match')

    # condition points (important for numerical reasons)
    # --from points--
    m = mean(fp[:2], axis=1)
    maxstd = max(std(fp[:2], axis=1)) + 1e-9
    C1 = diag([1/maxstd, 1/maxstd, 1])
    C1[0][2] = -m[0]/maxstd
    C1[1][2] = -m[1]/maxstd
    fp = dot(C1, fp)

    # --to points--
    m = mean(tp[:2], axis=1)
    maxstd = max(std(tp[:2], axis=1)) + 1e-9
    C2 = diag([1/maxstd, 1/maxstd, 1])
    C2[0][2] = -m[0]/maxstd
    C2[1][2] = -m[1]/maxstd
    tp = dot(C2, tp)

    # create matrix for linear method, 2 rows for each correspondence pair
    nbr_correspondences = fp.shape[1]
    A = zeros((2*nbr_correspondences, 9))
    for i in range(nbr_correspondences):
        # fill in the odd rows (1st row, 3rd row and so on)
        A[2*i] = [
            -fp[0][i],
            -fp[1][i],
            -1,
            0,
            0,
            0,
            tp[0][i]*fp[0][i],
            tp[0][i]*fp[1][i],
            tp[0][i]
        ]

        # fill in the even rows(2nd row, 4th row and so on)
        A[2*i + 1] = [
            0,
            0,
            0,
            -fp[0][i],
            -fp[1][i],
            -1,
            tp[1][i]*fp[0][i],
            tp[1][i]*fp[1][i],
            tp[1][i]
        ]

    U, S, V = linalg.svd(A)
    H = V[8].reshape((3, 3))

    # decondition
    H = dot(linalg.inv(C2), dot(H, C1))

    # normalize and return
    return H / H[2, 2]

def Haffine_from_points(fp, tp):
    """ Find H, affine transformation, such that
    tp is affine transf of fp. """
    if fp.shape != tp.shape:
        raise RuntimeError('number of points do not match')

    # condition points
    # --from points--
    m = mean(
        fp[:2],
        axis=1
    )

    maxstd = max( std(
        fp[:2],
        axis=1
    ) ) + 1e-9

    C1 = diag([1/maxstd, 1/maxstd, 1])
    C1[0][2] = -m[0]/maxstd
    C1[1][2] = -m[1]/maxstd
    fp_cond = dot(
        C1,
        fp
    )

    # --to points--
    m = mean(
        tp[:2],
        axis=1
    )

    C2 = C1.copy() # must use some scaling for point sets
    C2[0][2] = -m[0]/maxstd
    C2[1][2] = -m[1]/maxstd
    tp_cond = dot(
        C2,
        tp
    )

    # conditioned points have mean zero, so translation is zero
    A = concatenate(
        (
            fp_cond[:2],
            tp_cond[:2]
        ),
        axis = 0
    )
    U, S, V = linalg.svd( A.T )

    # create B and C matrices as Hartley-Zisserman (2:nd ed) p 130
    tmp = V[:2].T
    B = tmp[:2]
    C = tmp[2:4]

    tmp2 = concatenate(
        (
            dot(
                C,
                linalg.pinv(B)
            ),
            zeros( (2,1) )
        ),
        axis = 1
    )
    H = vstack(
        (
            tmp2,
            [0,0,1]
        )
    )

    # decondition
    H - dot(
        linalg.inv( C2 ),
        dot(
            H,
            C1
        )
    )

    return H / H[ 2, 2 ]


def image_in_image(im1, im2, tp):
    """ Put im1 in im2 with an affine transformation
    such that corners are as close to tp as possible.
    tp are homogeneous and counterclockwise from top left. """

    # points to warp from
    m, n = im1.shape[:2]
    fp = array(
        [
            [0, m, n, 0],
            [0, 0, n, n],
            [1, 1, 1, 1]
        ]
    )

    # compute affine transform and apply
    H = Haffine_from_points( tp, fp )
    im1_t = ndimage.affine_transform(
        im1,
        H[ :2, :2 ],
        ( H[ 0, 2 ], H[ 1, 2 ] ),
        im2.shape[ :2 ]
    )
    alpha = ( im1_t > 0 )

    return (1-alpha)*im2  + alpha*im1_t


def compute_harris_response(im_type_ndarray, sigma_type_int=3):
    """ Compute the harris corner detector response function
    for each pixel in a graylevel image. """

    # derivatives
    imx_type_ndarray = zeros( im_type_ndarray.shape )
    # compute the image derivative in the x direction, stored in imx_type_ndarray
    # imx_type_ndarray has the same shape as im_type_ndarray, which for the data/empire.jpg example is 183 rows, 275 columns
    # aka 275 x 183 pixels ( x x y pixels)
    filters.gaussian_filter(
        im_type_ndarray,
        (sigma_type_int, sigma_type_int),
        (0, 1),
        imx_type_ndarray
    )

    imy_type_ndarray = zeros( im_type_ndarray.shape )
    filters.gaussian_filter(
        im_type_ndarray,
        (sigma_type_int, sigma_type_int),
        (1, 0),
        imy_type_ndarray
    )

    # compute components of the Harris matrix
    # note that ndarray * ndarray is an element wise multiplication of the two matrices
    Wxx_type_ndarray = filters.gaussian_filter(
        imx_type_ndarray * imx_type_ndarray,
        sigma_type_int
    )

    Wxy_type_ndarray = filters.gaussian_filter(
        imx_type_ndarray * imy_type_ndarray,
        sigma_type_int
    )

    Wyy_type_ndarray = filters.gaussian_filter(
        imy_type_ndarray * imy_type_ndarray,
        sigma_type_int
    )

    # determinant and trace (same size as im_type_ndarray) which in this example is 275 x 183 pixels
    Wdet_type_ndarray = ( Wxx_type_ndarray * Wyy_type_ndarray ) - ( Wxy_type_ndarray**2 )
    Wtr_type_ndarray = Wxx_type_ndarray + Wyy_type_ndarray

    # compute element-wise division between determinant and trace matrices
    return Wdet_type_ndarray / Wtr_type_ndarray

def get_harris_points(harrisim_type_ndarray, min_dist_type_int=10, threshold_type_float=0.1):
    """ Return corners from a Harris response image
    min_dist is the minimum number of pixels separating
    corners and image boundary. """

    # find top corner candidates above a threshold
    corner_threshold_type_float = harrisim_type_ndarray.max() * threshold_type_float
    # convert from false/true to 0/1
    harrisim_t_type_ndarray = ( harrisim_type_ndarray > corner_threshold_type_float ) * 1

    # get coordinates of candidates
    coords_type_nddaray = array( harrisim_t_type_ndarray.nonzero() ).T

    # ...and their values
    candidate_values_type_list = [ harrisim_type_ndarray[
                                       c[0],
                                       c[1]
                                   ] for c in coords_type_nddaray]

    # sort candidates
    index_type_ndarray = argsort( candidate_values_type_list )

    # store allowed point locations in array
    allowed_locations_type_ndarray = zeros(harrisim_type_ndarray.shape)
    allowed_locations_type_ndarray[
        min_dist_type_int:-min_dist_type_int,
        min_dist_type_int:-min_dist_type_int
    ] = 1

    # select the best points taking min_distance into account
    filtered_coords_type_list = []
    for i in index_type_ndarray:
        if allowed_locations_type_ndarray[ coords_type_nddaray[ i, 0 ], coords_type_nddaray[ i, 1 ] ] == 1:
            filtered_coords_type_list.append( coords_type_nddaray[ i ] )
            allowed_locations_type_ndarray[
                ( coords_type_nddaray[ i, 0 ] - min_dist_type_int ):( coords_type_nddaray[ i, 0 ] + min_dist_type_int ),
                ( coords_type_nddaray[ i, 1 ] - min_dist_type_int ):( coords_type_nddaray[ i, 1 ] + min_dist_type_int )
            ] = 0

    return filtered_coords_type_list

def plot_harris_points(image_type_ndarray, filtered_coords_type_list):
    """ Plots corners found in image. """

    figure()
    gray()
    imshow( image_type_ndarray )
    plot(
        [p[1] for p in filtered_coords_type_list],
        [p[0] for p in filtered_coords_type_list],
        '*'
    )
    axis( 'off' )
    show()

im_type_ndarray = array( Image.open( 'data/empire.jpg' ).convert( 'L' ) )
harrisim_type_ndarray = compute_harris_response( im_type_ndarray )
filtered_coords_type_list = get_harris_points(
    harrisim_type_ndarray,
    min_dist_type_int=6
)
plot_harris_points(
    im_type_ndarray,
    filtered_coords_type_list
)

