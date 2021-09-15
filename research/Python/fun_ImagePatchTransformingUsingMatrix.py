from numpy import array
from PIL import Image
from scipy import ndimage
from matplotlib.pyplot import figure, gray, imshow, show


im_type_ndarray = array(
    Image.open('data/empire.jpg').convert('L')
)
H_type_ndarray = array(
    [
        [ 1.4, 0.05, -100 ],
        [ 0.05, 1.5, -100 ],
        [ 0, 0, 1 ]
    ]
)

im2_type_ndarray = ndimage.affine_transform(
    im_type_ndarray,
    H_type_ndarray[ :2, :2 ],
    ( H_type_ndarray[ 0, 2 ], H_type_ndarray[ 1, 2 ] )
)

# zeros are black

figure()
gray()
imshow(im2_type_ndarray)
show()


