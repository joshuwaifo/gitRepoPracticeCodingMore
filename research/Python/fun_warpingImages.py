try:
    import warp
    from numpy import array
    from PIL import Image
    from matplotlib.pyplot import figure, gray, imshow, axis, show

    # example of affine warp of im1 onto im2
    im1 = array( Image.open( 'beatles.jpg' ).convert( 'L' ) )
    im2 = array( Image.open( 'billboard_for_rent.jpg' ).convert( 'L' ) )

    # set to points
    tp = array(
        [
            [ 264, 538, 540, 264 ],
            [ 40, 36, 605, 605 ]
        ]
    )

    im3 = warp.image_in_image( im1, im2, tp )

    figure()
    gray()
    imshow( im3 )
    axis( 'equal' )
    axis( 'off' )
    show()
except Exception:
    print( "debug the importing of warp and get the beatles.jpg and billboard_for_rent.jpg images" )

from numpy import array
tp = array(
    [
        [ 675, 826, 826, 677 ],
        [ 55, 52, 281, 277 ],
        [ 1, 1, 1, 1 ]
    ]
)

try:
    import homography
    from scipy import ndimage
    # set from points to corner of im1
    m, n = im1.shape[ :2 ]
    fp = array(
        [
            [ 0, m, m, 0 ],
            [ 0, 0, n, n ],
            [ 1, 1, 1, 1 ]
        ]
    )

    # first triangle
    tp2 = tp[ :, :3 ]
    fp2 = fp[ :, :3 ]

    # compute H
    H = homography.Haffine_from_points( tp2, fp2 )
    im1_t = ndimage.affine_transform(
        im1,
        H[ :2, :2 ],
        ( H[ 0, 2 ], H[ 1, 2 ]),
        im2.shape[ :2 ]
    )

    # alpha for triangle
    alpha = warp.alpha_for_triangle(
        tp2,
        im2.shape[ 0 ],
        im2.shape[ 1 ]
    )
    im3 = ( ( 1 - alpha ) * im2 ) + ( alpha * im1_t )

    # second triangle
    tp2 = tp[ :, [ 0, 2, 3 ] ]
    fp2 = tp[ :, [ 0, 2, 3 ] ]
except Exception:
    print( "need to debug the importing of homography and the use of warp")