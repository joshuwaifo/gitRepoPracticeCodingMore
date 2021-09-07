# some points
x = [ 100, 100, 400, 400 ]
y = [ 200, 500, 200, 500 ]

# plot the points
try:
    plot( x, y)
except NameError:
    print("The function plot is not available at the moment")


from PIL import Image
import os

pil_im_type_JpegImageFile = Image.open('data/empire.jpg')
pil_im_type_Image = Image.open('data/empire.jpg').convert('L')

try:
    for infile in filelist:
        outfile = os.path.splittext(infile)[0] + ".jpg"
        if infile != outfile:
            try:
                Image.open(infile).save(outfile)
            except IOError:
                print(f"cannot covert {infile}")
except NameError:
    print("There is no variable called filelist defined at the moment")


def get_imlist(path):
    """ Returns a list of filenames for all jpg images in a directory. """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


from PIL import Image
from pylab import *

# read image to array
im_type_ndarray = array( Image.open( 'data/empire.jpg' ).convert( 'L' ) )

# create a new figure
figure()
# don't use colors
gray()
# show contours with origin upper left corner
contour( im_type_ndarray, origin = 'image' )
axis( 'equal' )
axis( 'off' )

figure()
hist( im_type_ndarray.flatten(), 128 )
show()