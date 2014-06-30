# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 15:34:58 2014

@author: Maria
"""

#finding pixel values
from astropy.io import fits
import os
from numpy import *


def pixel_ext(target_dir,image):
    #change directory    
    os.chdir(target_dir)
    
    #creates lists of images 
    y_images,add = Y_sections(image,target_dir)
    x_images = X_sections(image,target_dir)
    com_images = array(x_images) + array(y_images)
    print com_images
    median_fits(com_images, add + "sky_medain.fits",add)    
    
    
    
def Y_sections(image, path):    
    new_images = []    
    for j in range(0,3880,10):
        k = 10+j
        x1 = 2006
        x2 = 2016            
        x = os.path.join(path,image)
        f = fits.open(x)        
        d = f[0].data
        section = d[j:k,x1:x2]
        new_images.append(section)
        c = f[0].header['filter']
        f.close()
        
    return new_images,c


def X_sections(image, path):    
    new_images = []    
    for j in range(0,3880,10):
        k = 10+j
        y2 = 3550
        y1 = 3540            
        x = os.path.join(path,image)
        f1 = fits.open(x)        
        d1 = f1[0].data
        section = d1[y1:y2,j:k]
        new_images.append(section)
        f1.close()
        
    return new_images
    
    
##########
# DESCRIPTION
#     Creates a new header card called filter and sets it equal to 'Ha 6620'
# PARAMETERS
#     x      - tells function where file is with path joined with filename
#     f      - opened fits file in update mode
#     keyword- card you'd like to add to the header
#     phrase - what you want to be stored in the header card
##########    
    
def new_headercard(image,path,keyword ="",phrase=""):
    #for i in images:
    x = os.path.join(path,image)
    f2= fits.open(x, mode ='update')
    f2[0].header[keyword] = phrase
    f2.flush()
    f2.close()



def median_fits(data_list,newfile_name="",add =""):
    dm = data_list

    #axis 0 is the intensity
    med =  median(dm, axis = 0)
    path2 = '/nfs/home/mcqu4304/maskims/No_obs'
    hdu = fits.PrimaryHDU(med)
    hdulist = fits.HDUList(hdu)
    
    #creates the new file name
    newimage = os.path.join(path2, newfile_name)
    hdulist.writeto(newimage)
    
    
    #new_headercard(newimage,"'/nfs/home/mcqu4304/maskims/No_obs'","OBJECT",add+"sky_median")
    
    return newfile_name
        
pixel_ext('/nfs/home/mcqu4304/maskims/No_obs','noobstrimHacombined_5.fits') 