from PIL import Image, ImageFilter




# FILTERING
from scipy import ndimage
import scipy.ndimage as nd
import numpy as np
import matplotlib.pyplot as plt


im = Image.open( 'ball_in_rough.jpg' )

im2 = im.filter(ImageFilter.MinFilter)
im2.save('ball_proc.jpg')


im = nd.imread('ball_proc.jpg', True)
im = im.astype('int32')
dx = nd.sobel(im,1)
dy = nd.sobel(im,0)
mag = np.hypot(dx,dy)
mag *= 255.0/np.max(mag) 

fig, ax = plt.subplots()
ax.imshow(mag, cmap = 'gray')
plt.xticks([]), plt.yticks([])
plt.savefig('sobel.jpg')
