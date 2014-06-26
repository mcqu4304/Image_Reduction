# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Maria\.spyder2\.temp.py
"""
##########
# DESCRIPTION
#	Starts at base_path and calls a variety of functions defined below
# PARAMETERS
#	base_path - where you want the program to start running
#	images - the fits files in the current path
# RETURNS
#	nothing
##########
import os
from astropy.io import fits
from numpy import * 
def main():
    
    base_path = 'C:\Users\Maria\Physics_Research\Attemp_3\Registered_Ims_3'
    os.chdir(base_path)
    print os.getcwd()
    files = os.listdir(base_path)      
    images = sort(files)
    #Ovs_sub(images)
    imtrim(images)

#main()    

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
#    opens the file -> acesses the data -> choses the sections of the overscan ->
#    unravles the arrays so they are both 1D and horizontally stacks them ->
#    computes the median and subratcs it from the orginal data.
# PARAMETERS
#    f1      - file you want to change or manipulate. 
#    d1  - data in the file
#    hdu     - creates a new primaryheader to store the data from output2 in the 
#              primary position and copies the header from the original file.
#    section1- the first section of the data
#    section2- the second section of the data
#    a       - unravels the array in section1 to 1D
#    b       - unravels the array in section2 to 1D
#    s       - the stacked arrays
#    m       - median value of s
#    ovmedian- an array of ones multiplied by the median
#    output  - the subtraction of the medain value from the orignial data
#    images  - list of fits files in the current working directory
# RETURNS
#    none
##########
  
def Ovs_sub(images):
    for i in images:
        f1 = fits.open(i)
        d1 = f1[1].data
        section1 = d1[4096:4150,0:4150] 
        section2 = d1[0:4096,4096:4150]
        a = section1.ravel()
        b = section2.ravel()
        s = hstack((a,b))
        m = median(s)
        ovmedian = ones((4150,4150))*m
        output = d1 - ovmedian
        hdu = fits.PrimaryHDU(output,f1[0].header)
        hdu.writeto('OvS1'+ i)
        f1.close()

##########
# DISCRIPTION
#    loops through images and opens the files -> picks a portion of the image -> 
#    print the shape of the new array -> saves trimed array into a new fits 
#    file with the old header.
# PARAMETERS
#    f1      - file you want to change or manipulate. 
#    section - the trimed data with in the boundaries of the trim.
#    hdu     - creates a new primaryheader to store the data from output in the 
#              primary position and copies the header from the original file.
#    images  - list of fits files in the current working directory
# RETURNS
#    none
##########
    
def imtrim(images):
    for i in images:
        f1 = fits.open(i)
        d1 = f1[0].data
        section = d1[197:4096,0:4031]  
        print section.shape   
        hdu = fits.PrimaryHDU(section)
        hdulist = fits.HDUList([hdu])
        hdulist.writeto('trim'+ i)
        f1.close()

if __name__=='__main__': main()