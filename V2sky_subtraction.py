# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 14:45:19 2014

@author: Maria
"""
import os
from astropy.io import fits
import subprocess
import sys 
target_dir = "/nfs/home/mcqu4304/
filename = "back.fits"

def main(target_dir):
    files = os.listdir(target_dir, filename)
    images = sort(files)
    for i in images:
        subprocess.call(sex,i)
        f = fits.open(i)
        d = f[0].data[:]- filename
        hdu = fits.PrimaryHDU(d,f[0].header)
        hdulist = fits.HDUList([hdu])
        newimage = os.path.join(target_dir, "back_sub")
        hdulist.writeto(newimage)
        os.remove(filename)
        
    
def sort(files):
    images = []
    for i in files:
        [name, ext] = os.path.splitext(i)
        if ext == '.fits' or ext == '.fit' or ext == '.fts':
            images.append(i)		
    return images
    
# Invoke the main loop
if __name__ == "__main__":
   sys.exit(main(target_dir))