# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 08:43:34 2014

@author: Maria
"""
import os
from pyraf import iraf
import sys
import tempfile
from astropy.io import fits



def main(target_dir,no_unlearn = False):    
    #create a mask for images  
    files = os.listdir(target_dir)
    images = sort(files)
    images = [os.path.join(target_dir,i) for i in images]
    new_images = mask_create(images,no_unlearn=no_unlearn)
    print new_images    
    fix_mask(new_images)

    
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

def mask_create(images, no_unlearn = False):
    output_files =[] 
    # If the output file list doesn't exsist, create it.    
    if len(output_files) == 0:
       output_files = [os.path.join(os.path.dirname(i), 'mask_' + os.path.basename(i)) for i in images]
    # Create a temporary file to hold the input image list
    tfile = tempfile.mkstemp()
    os.write(tfile[0],"\n".join(images)+"\n")
    os.close(tfile[0])
    
    # Create a temporary file to hold the input image list
    tofile = tempfile.mkstemp()
    os.write(tfile[0],"\n".join(output_files)+"\n")
    os.close(tfile[0])

    try:

        # Set up to call the task
        iraf.set(clobber='yes')
        iraf.nproto()

        if no_unlearn == False:
            print "Objmasks is unlearning!!"
            iraf.objmasks.unlearn()
            
        #set parameters
        iraf.objmasks.images = "@" + tfile[1]
        iraf.objmasks.objmasks = "@" + tofile[1]
        iraf.objmasks.omtype = "boolean"
        iraf.objmasks()
                    
    except iraf.IrafError, e:
            print "objmasks failed"
            print "error #" + str(e.errno)
            print "Msg: " + e.errmsg
            print "Task: " + e.errtask
            raise e
    finally:
            os.remove(tfile[1])		# remove the tempfile
            os.remove(tofile[1])
            

    return output_files

def fix_mask(new_images):   
    for k in new_images:
        #x = os.path.join(target_dir,k)
        f = fits.open(k)
        # fix the header card PONTIME since it's not FITS standard
        f.verify('fix')
        d= f[1].data
        print type(d)
        for i in range(len(d)):
            for j in range(len(d)):
                if d[i,j] == 0:
                    d[i,j] = 1
                elif d[i,j] == 1:
                    d[i,j] = 0
    
        hdu = fits.PrimaryHDU(d)
        hdu.writeto('Fix'+ k)
    
        f.close()
target_dir = "/nfs/home/mcqu4304/maskims"
no_unlearn = False    
main(target_dir,no_unlearn=no_unlearn)