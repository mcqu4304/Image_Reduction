# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Maria\.spyder2\.temp.py
"""
##########
# DESCRIPTION
#    opens fits files and saves data into varibles
# PARAMETERES
#    filename1 and filename2 will be the files you
#    want to open and get data from.
# RETURNS:
#    d1 - array stored in filename1. 
#    d2 - array stored in filename2.
##########
from astropy.io import fits
def open_fits(filename1,filename2):
    f1 = fits.open(filename1)
    f2 = fits.open(filename2)
    d1 = f1[0].data 
    d2 = f2[0].data
    return d1,d2
    
##########
# DESCRIPTION
#    change header "cmmtobs' and 'object' in the input file -> write changes
#    to the original file.
# PARAMETERES
#    f       - opened file in update mode. 
#    prihdr  - header in the primary position.
#    f.flush - save the updated file.
# RETURNS
#    none
##########
def change_header(fil):
    f = fits.open(fil, mode = 'update') 
    prihdr = f[0].header
    #headers you want to change
    prihdr['cmmtobs'] = 'NGC 2799 B'
    prihdr['object'] = 'NGC 2799 B'
    f.flush()
    f.close()
    ###
    # Check is the file changed
    ###
    prihdr= f[0].header
    #the header you changed
    headername = 'object'
    #shows what was set to the header
    print prihdr[headername]
"""change_header('c6747t0043o00.fits')"""

##########
# DESCRIPTION
#    adds or appends the card, 'headername' -> 
#    writes (header attribute, comment) ->
#    saves the file and closes it.
# PARAMETERS
#    f       - opened file in update mode. 
#    prihdr  - header in the primary position.
#    f.flush - save the updated file.
# RETURNS
#    none
##########
def append_header(fil):
    f = fits.open(fil, mode='update')
    prihdr=f[0].header
    #header you wanted to add and comments
    prihdr['object'] = ('Median Bias Frame',\
    'the median of the the bias frames')
    f.flush()
    f.close()
    """shows what was set to the header"""
    #print prihdr['object']



##########
# DESCRIPTION
#    subtracts two images and saves them to a new fits file.
"""note: if the first file already has the desired header information use 
f1[].header instead of f2[].header you"""
# PARAMETERS
#    f1        - file you want to change or manipulate. 
#    f2        - file you are using to change the other. 
#    output    - difference of the two files.
#    hdu       - creates a new primaryheader to store the data from output in the 
#                primary position and copies the header from f2. 
#    filename3 - name of the file you want to save it to.
# RETURNS
#    none
##########
output = 0
def image_subtraction(image1,image2):
    f1 = fits.open(image1)
    f2 = fits.open(image2)
    output = f1[1].data - f2[0].data
    hdu = fits.PrimaryHDU(output, f2[0].header)
    hdu.writeto('sub'+ image1)
    """save the data into a new file"""
    hdu = fits.PrimaryHDU(output)
    filename3 = "subtractedimage"
    hdu.writeto(filename3)

##########
# DESCRIPTION
#    divides two images and saves them to a new fits file.
"""note: if the first file already has the desired header information use 
f1[].header instead of f2[].header you"""
# PARAMETERS
#    f1        - file you want to change or manipulate. 
#    f2        - file you are using to change the other. 
#    output1   - division of the two files.
#    hdu       - creates a new primaryheader to store the data from output1 in the 
#                primary position and copies the header from f2. 
#    filename4 - name of the file you want to save it to.
# RETURNS
#    none
##########
output1 = 0
def image_division(image1,image2):
    f1 = fits.open(image1)
    f2 = fits.open(image2)
    output1 = f1[1].data/f2[1].data
    print output1
    """saves the divieded array into a new fits file"""
    hdu = fits.PrimaryHDU(output1,f2[0].header)
    filename4 = "subtractedimage"
    hdu.writeto(filename4)

###########
# DESCRIPTION
#    finds the stadard deviation of the pixel values in an image then closes
#    the file.
# PARAMETERS 
#    f - open fits file. 
#    s - standad deviation of the data in f.
# RETURNS
#    none
##########
import numpy as np
def std_of_plv(image,header_pos = 0):
    f = fits.open(image)
    s = np.std(f[header_pos].data)
    print s
    f.close()
"""std_of_plv('nsat_median.fits')"""

##########
# DESCRIPTION
#    normalizes an image and saves the data and original header to a new 
#    fits file then closes the file.
# PARAMETERS
#    f       - file you want to change or manipulate. 
#    output2 - normalized data. 
#    hdu     - creates a new primaryheader to store the data from output2 in the 
#              primary position and copies the header from the original file.
# RETURNS
#    none
##########
def normalize(fil,header_pos):
    f = fits.open(fil)
    d = f[header_pos].data
    output2= d/np.linalg.norm(d)
    hdu = fits.PrimaryHDU(output2,f[head_pos].header)
    add = 'norm'
    hdu.writeto(add + fil)
    f.cose()
'''normalize('average_bflat.fits')'''

##########
# DESCRIPTION
#     Creates a new header card called filter and sets it equal to 'Ha 6620'
# PARAMETERS
#     x      - tells function where file is with path joined with filename
#     f      - opened fits file in update mode
#     keyword- card you'd like to add to the header
#     phrase - what you want to be stored in the header card
#     header_pos - the position in the header where the desired information 
#                  is stored, usually 0 but can be 1
########## 
def new_headercard(images,path,header_pos = 0, keyword="",phrase=""):
    for i in images:
        x = os.path.join(path,i)
        f= fits.open(x, mode ='update')
        f[header_pos].header[keyword] = phrase
        f.flush()
        f.close()

##########
# DESCRIPTION
#    opens a fits file-> displays some header info -> stores data into
#    the variable f -> picks out pieces of the code in the first column ->
#    plots the data in a scatter plot -> closes the file.
# PARAMETERS
#    f     - fits file. 
#    fdata - data within the file. 
#    xi    - value at the specified location.
# RETURNS
#    none
##########
from pylab import *
import matplotlib.pyplot as plt
def data_plot(fil):
    f = fits.open(fil)
    f.info()
    #access data from image file.
    #contains actual elements of the array
    fdata = f[1].data
    for i in range(5):
        xi = fdata[i,0]
        print xi
        plt.scatter(xi,xi)
        #turns on a grid
        grid(True)
        xlabel('x')
        ylabel('y')
        title('Title')
    #display the plot
    plt.show()
    f.close()










