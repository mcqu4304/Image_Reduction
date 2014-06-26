# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Maria\.spyder2\.temp.py
"""

from astropy.io import fits
from numpy import *
  
##########
# DESCRIPTION
#	Starts at base_path and calls the sort function -> calls image_division, 
#     image_subtraction or nomalize
# PARAMETERS
#	base_path - where you want the program to start running
#	images - the fits files in the current path
#	image2 - the image used to change the file called from images
# RETURNS
#	nothing
##########
import os
def main():
    # sets the code to look at the files in this directory
    base_path = 'C:\Users\Maria\Physics_Research'
    os.chdir(base_path)
    files = os.listdir(base_path)
    print os.getcwd()     
    images = sort(files)
    #image2 = 'normaverage_bflat.fits'
    #image_division(images,'normaverage_rflat.fits')
    #image_subtraction(images,'Master_Bias.fits')
    normalize(images)
    #mean_image(images)

##########
# DESCRIPTION
#	Sorts the images in the current folder so that you're left with fits files only
# PARAMETERS
#	images - list of fits files in the current working directory
# RETURNS
#	images
##########

def sort(files):
    images = []

    for i in files:
        [name, ext] = os.path.splitext(i)
        if ext == '.fits' or ext == '.fit' or ext == '.fts':
            images.append(i)		
    return images	
    
##########
# DISCRIPTION
#    subtracts two images and saves them to a new fits file with the old header.
    """note: if the first file already has the desired header information use 
       f1[].header instead of f2[].header you"""
# PARAMETERS
#    f1        - file you want to change or manipulate. 
#    f2        - file you are using to change the other. 
#    images - list of fits files in the current working directory    
#    output    - the difference of the two files.
#    hdu       - creates a new primaryheader to store the data from output in  
#                the primary position and copies the header from f2. 
#    i         - the file from images
# RETURNS
#    none
##########
    
output = 0
def image_subtraction(images,image2):
    for i in images:
        f1 = fits.open(i)
        f2 = fits.open(image2)
        output = f1[0].data - f2[0].data
        hdu = fits.PrimaryHDU(output,f1[0].header)
        hdu.writeto('Bsub'+ i)
        f1.close()
        f2.close()

##########
# DISCRIPTION
#    divides two images and saves them to a new fits file with the old header.
    """note: if the first file already has the desired header information use 
       f1[].header instead of f2[].header you"""
# PARAMETERS
#    f1        - file you want to change or manipulate. 
#    f2        - file you are using to change the other. 
#    images - list of fits files in the current working directory 
#    output    - the division of the two files.
#    hdu       - creates a new primaryheader to store the data from output in  
#                the primary position and copies the header from f2. 
#    add       - the string addtion you want to add to the new file
#    i         - the file from images
# RETURNS
#    none
##########
output1 = 0
def image_division(images,image2):
    for i in images:    
        f1 = fits.open(i)
        f2 = fits.open(image2)
        output1 = f1[0].data/f2[0].data
        hdu = fits.PrimaryHDU(output1,f1[0].header)
        add = 'Final'
        hdu.writeto(add + i)
        f1.close()
        f2.close()

##########
# DISCRIPTION
#    normalizes an image and saves the data and original header to a new 
#    fits file then closes the file.
    """note: you don't need the second file if the first file already has the 
       desired header information. instead of f2[].header you would use 
       f1[].header. you will also need to change the calling arguments to 
       exclude the second calling argument"""
# PARAMETERS
#    f       - file you want to change or manipulate. 
#    output2 - normalized data. 
#    hdu     - creates a new primaryheader to store the data from output2 in the 
#              primary position and copies the header from the original file.
#    add     - the string addtion you want to add to the new file
#    images  - list of fits files in the current working directory
# RETURNS
#    none
##########

def normalize(images):
    for i in images:
        f = fits.open(i)
        d = f[1].data
        output2= d/d.mean()
        hdu = fits.PrimaryHDU(output2,f[0].header)
        hdu.writeto("norm" + i)
        f.close()

##########
# DISCRIPTION
#    finds the mean image by looping through the list of images to add them
#    and dividing by the length of the list and saves the data to a new 
#    fits file then closes the file.
# PARAMETERS
#    f       - file you want to change or manipulate. 
#    output  - mean data. 
#    d       - data in the fits file
#    s       - sum of the images
#    n       - length of the list
#    a       - an array of ones that is the same size as the image files
#    hdu     - creates a new primaryheader to store the data from output2 in the 
#              primary position and copies the header from the original file.
#    images  - list of fits files in the current working directory
# RETURNS
#    none
##########    
    
def mean_image(images):
    s = 0
    for i in images:
        f = fits.open(i)
        d = f[0].data
        s = s + d
        f.close()
    print s
    a = ones((4150,4150))
    n = len(images)
    a = a*n
    output = s/a
    hdu = fits.PrimaryHDU(output)
    hdu.writeto('average_haflat.fits')

# calls the main function after all funciton have been defined
if __name__=='__main__': main()    





            


          
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            