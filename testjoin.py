import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
import matplotlib as mpl
import sympy as smp
import numpy as np
import cv2
import os,glob

from os import listdir,makedirs
from os.path import isfile,join
from PIL import Image

source_folder1 = 'D:/datasetpicture/picture/test_resize/'
source_folder2 = 'D:/datasetpicture/picture/real_fourier640/'
target_folder = 'D:/datasetpicture/picture/real_compare/'

n = len(source_folder1)+1

for img_no in range(1,n+1):
    img1 = (source_folder1+str(img_no)+".jpg")
    img2 = (source_folder2+str(img_no)+".jpg")
    
    images = [Image.open(x) for x in [img1, img2]]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))


    x_offset = 0
    for im in images:
      new_im.paste(im, (x_offset,0))
      x_offset += im.size[0]

    new_im.save(target_folder+str(img_no)+".jpg")