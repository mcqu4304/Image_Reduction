# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Maria\.spyder2\.temp.py
"""

from astropy.io import fits
import os
##########
# DESCRIPTION
#	Add a prefix to a filename, in this case it adds the filter color.
# PARAMETERS
#	base_path - where you want the program to start running
#	images - the fits files in the current path
# RETURNS
#	nothing
##########
def main():
    base_path = "C:\Users\Maria\Physics_Research"
    os.chdir(base_path)
    files = os.listdir(base_path)
    #print os.getcwd()
    images = sort(files,base_path)
    # ( __ , path) gives the path to look in 
    list_files(images,base_path)

##########
# DESCRIPTION
#	Sorts the images in the current folder so that you're left with fits files only
# PARAMETERS
#	images - list of fits files in the current working directory
# RETURNS
#	images
##########    
def sort(files,path):
    images = []
    for i in files:
        [name, ext] = os.path.splitext(i)
        if ext == '.fits' or ext == '.fit' or ext == '.fts':
            images.append(i)		
    return images	

###########
# DESCRIPTION
#     gets the filter name from the header and adds it to the front of the 
#     filename.
# PARAMETERS
#     x       - joins the path with the image.
#     f1      - opens up the image in the specified path
#     path2   - the place you want to put the new file
#     hdu     - creates a new primary header and copies the old one into it
#     head    - the fits header
#     hdulist - the composition of all header cards
#     i       - new name with add on
#     newimage- tels the new file where to save it
# RETURNS
#     none
###########       
def list_files(images,path):
    
    for i in images:
        #joins path with image so it knows where to find it
        dir = path+ "\Filter_files"
        try:
            os.stat(dir)
        except:
            os.mkdir(dir) 
        x = os.path.join(dir,i)
        f1 = fits.open(x)
        head = f1[0].header
        filt_str = head['filter']
        #can create file in a different location            
        path2 = dir
        hdu = fits.PrimaryHDU(f1[0].data,f1[0].header)
        hdulist = fits.HDUList(hdu)
        #creates the new file name
        i = filt_str + i
        newimage = os.path.join(path2, i)
        hdulist.writeto(newimage)
        
        f1.close()
        


if __name__=='__main__': main() 