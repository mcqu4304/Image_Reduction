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
#	Sets the program to look at the base path. joins the files with paths.
#     calls sort() to sort the images. calls get_filters to get a list of filters
#     loops through the images checked their headers for the filter both wheel
#     positions and interprets the information to tell filter color or if there
#     is an error or if it is a BIAS or DARK.
#
# PARAMETERS
#	base_path - where you want the program to start running
#	images    - the fits files in the current path
#     filters   - list of filters given from a text file
#     pfiles    - list of files with paths
#     w1        - position of the 1st wheel
#     w2        - position of the 2nd wheel
#     x2        - string containing the filter name from wheel 2
#     x1        - string containing the filter name from wheel 1
#     f         - opens fits file in update mode
#     obstype   - the object type from the header
# RETURNS
#	nothing
##########

check_keyword = "FILTER1"

def main(check_keyword):
    base_path = 'C:\Users\Maria\Physics_Research\mar28_14\Renamed'
    os.chdir(base_path)
    files = os.listdir(base_path)  
    images = sort(files)
    filters = get_filters("filtertest.txt")    
    for i in images:
        w1 = wheel_1(i,'FILTER1')
        w2 = wheel_2(i,'FILTER2')
        print w1
        print w2
        f1 = fits.open(i)
        obstype = f1[0].header['OBSTYPE']
        #if keyword is in the header
        if check_keyword in f1[0].header.keys():        
            #Dark images have no filer1 or filter2 in header        
            if obstype != "DARK" and obstype != "BIAS":
                
            
                if filters[w1] == "0" and filters[w2] == "0":
                    print i                    
                    print "ERROR: Both Wheels EMPTY"    
                           
                if filters[w1] != "0" and filters[w2] != "0":
                    print i
                    print "ERROR: Neither Wheel is EMPTY"
                
                elif filters[w1] == "0":
                    print i
                    x2 = filters[w2]           
                    f = fits.open(i, mode = 'update')
                    
                    f[0].header['filter'] = x2
                    f.flush()
                    f.close()
            
                elif filters[w2] == "0":
                    print i
                    x1 = filters[w1]
                    f = fits.open(i, mode = 'update')
                    f[0].header['filter'] = x1
                    f.flush()
                    f.close()
                    
            else:
                print i
                f = fits.open(i, mode = 'update')
                f[0].header['filter'] = "NONE" 
                f.flush()
                f.close()
                print obstype
        
        else:
            print "ERROR: No information"
    # if you'd like the filter information to be printed in the filename    
    #list_files(images,base_path)
                    
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
#      creates a list of filters and fills it with information from a text file.
#      The information on the text file must be written in one column. 
#        For Example:
#        B
#        G
#        R
#        0
#        string
#        srting2
#      if the filter space is empty simply place a 0 in that spot in the text 
#      file.
# PARAMETERS
#      filefilts   - file object containing file information in read mode
#      filter_list - list of filter strings given from file
# RETURNS
#      filter_list - retunrs list of filters back to main
##########
def get_filters(filename):
    filter_list = []
    filefilts = open(filename,'r')
    #stores file info in filter_list    
    for i in filefilts:
        #stips all invisible characters from strings        
        i = i.strip()
        filter_list.append(i)
        
    return filter_list
       
##########
# DESCRIPTION
#     scans the header for the information in the header card FILTER1. stores
#     the information in f1.
# PARAMETERS
#     f    - open fits file
#     head - header of the file
#     f1   - string from FILTER1
# RETURNS
#     f1 - returns the string in FILTER1 to wheel_1 defined below
##########        
def headscan(i,keyword):
    f = fits.open(i)
    head = f[0].header
    f1 = head[keyword]
    #return string contained in FILTER1 
    return f1


##########
# DESCRIPTION
#      takes the string from the first filter wheel and extracts the last number
#      in the string.
# PARAMETERS
#      filt_str  - the string recorded in FILTER1
# RETURNS
#      returns the integer that matches the last character in the string back 
#      to main.
###########    
def wheel_1(i,keyword):
    filt_str = headscan(i,keyword)
    if filt_str[2] == "0":
        return 0
    if filt_str[2] == "1":
        return 1
    if filt_str[2] == "2":
        return 2
    if filt_str[2] == "3":
        return 3
    if filt_str[2] == "4":
        return 4
    if filt_str[2] == "5":
        return 5
    if filt_str[2] == "6":
        return 6
    if filt_str[2] == "7":
        return 7

##########
# DESCRIPTION
#      takes the string from the 2nd filter wheel and extracts the last number
#      in the string.
# PARAMETERS
#      filt_str  - the string recorded in FILTER2
# RETURNS
#      returns the integer that matches the last character in the string back 
#      to main.
##########                
def wheel_2(i,keyword):
   filt_str2 = headscan(i,keyword)
   if filt_str2[2] == "0":
       return 8
   if filt_str2[2] == "1":
       return 9
   if filt_str2[2] == "2":
       return 10
   if filt_str2[2] == "3":
       return 11
   if filt_str2[2] == "4":
       return 12
   if filt_str2[2] == "5":
       return 13
   if filt_str2[2] == "6":
       return 14
   if filt_str2[2] == "7":
       return 15

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
        dir = path+ "\Filenames_with_filters"
        try:
            os.stat(dir)
        except:
            os.mkdir(dir) 
        x = os.path.join(path,i)
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
           
if __name__=='__main__': main(check_keyword) 