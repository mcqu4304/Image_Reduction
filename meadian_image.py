# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 08:59:35 2014

@author: Maria
"""
from astropy.io import fits
from numpy import *
import os



########## I want to know how to tell if a header card is in a file if not then don't go on ######################3



target_dir = "C:\Users\Maria\Physics_Research\Ha_sections"
def main(target_dir):
    files = os.listdir(target_dir)
    images = sort(files)
    data_list = array_list(images,target_dir,'OBJECT','Not Satellite')
    new_headercard(median_fits(data_list,'nsat_median.fits'),"C:\Users\Maria\Physics_Research\Ha_sections",'OBJECT','Not Satellite')
    
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
# DESCRIPTION
#    
def array_list(images,path,keyword="",phrase=""):
    #list of data    
    arr_list = []    
    for i in images:
        x = os.path.join(path,i)
        f = fits.open(x)
        head = f[0].header
        
        #if keyword is in the header
        if keyword in head.keys():       
            # to filter what files you want to be part of the data
            if head[keyword] == phrase:
                d = f[0].data
                a = d[:,:]  # to grab a section of the data      
                arr_list.append(a)
    
    return arr_list
        
    
def median_fits(data_list,newfile_name=""):
    dm = array(data_list)

    #axis 0 is the intensity
    med =  median(dm, axis = 0)
    path2 = "C:\Users\Maria\Physics_Research\Ha_sections"
    hdu = fits.PrimaryHDU(med)
    hdulist = fits.HDUList(hdu)
    
    #creates the new file name
    newimage = os.path.join(path2, newfile_name)
    hdulist.writeto(newimage)
    
    return newfile_name

##########
# DESCRIPTION
#     Creates a new header card called filter and sets it equal to 'Ha 6620'
# PARAMETERS
#     x      - tells function where file is with path joined with filename
#     f      - opened fits file in update mode
#     keyword- card you'd like to add to the header
#     phrase - what you want to be stored in the header card
########## 
def new_headercard(image,path,keyword="",phrase=""):
    x = os.path.join(path,image)
    f= fits.open(x, mode ='update')
    f[0].header[keyword] = phrase
    f.flush()
    f.close()

if __name__=='__main__': main(target_dir) 
