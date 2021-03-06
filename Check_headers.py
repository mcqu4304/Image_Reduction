# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 10:20:51 2014

@author: Maria
"""

from astropy.io import fits
import os
####Take out hard coding of key words and make them arguments#######

##########
# DESCRIPTION
#	Starts at base_path and it will call functions that create a text catalog.
# PARAMETERS
#	base_path - where you want the program to start running
#	images - the fits files in the current path
#	list - calls the function that will write the text file
# RETURNS
#	nothing
##########

def main():
    base_path = 'C:\Users\Maria\Physics_Research\mar28_14\Renamed'
    os.chdir(base_path)
    print os.getcwd()
    files = os.listdir(base_path)    
    images = sort(files)
    file(images,"Check_header.txt")
            
            
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
#	Creates and writes into a file called catalog. It puts the iformation into
#     the text file.
# PARAMETERS
#	images - list of fits image names
#	filter - list of objects observed
#	exp    - list of exposure times
#	time   - list of times when the images were taken
#     air    - list of air mass
#     foc    - list of focuses
#     filenum- list of filenumbers 
# RETURNS
#	nothing
##########

def file(images,filename):
    filenum = filenum_build(images)
    filter = color_build(images)
    exp = exp_List_build(images)
    foc = Focus_build(images)    
    time = date_build(images)
    # if it already exists it will delete it and create a new one.
    if os.path.exists(filename):
        os.remove(filename)
    # creates a new catalog and puts into the variable info
    info = open(filename, "w")
    info.write("%10s,%25s,%10s,%15s,%30s\n" % ("Filename","Object","Filter","Exposure Time","Time Taken"))
    # wirtes information from lists into files
    for i in range(len(images)):
        info.write('%10s,' % filenum[i])
        info.write('%25s,' % filter[i])
        info.write('%10s,' % foc[i])
        info.write('%15s,' % exp[i])
        info.write('%30s,' % time[i])
        info.write('\n')                     
    info.close()
    
##########
# DESCRIPTION
#   builds a list called filnum that contains filenumbers
# PARAMETERS
#   filnum - list of filenumbers from filename()
# RETURNS
#   filnum - retruns list to file()
##########
def filenum_build(images):
    filnum = []
    for i in images:
	    filnum.append(filename(i))
    return filnum    

##########
# DESCRIPTION
#   loops through the filename and picks out the 4 character filenumber
# PARAMETERS
#   f - constructs the filenumber
# RETURNS
#   f - returns the filenumber back to filenum_build
##########
def filename(x):
    for i in x:
       f =""
       for j in range(len(x)):
           if j > 5 and j <10:
               f = f + x[j]
    return f
            
"""def extract(x):
    f =""
    for i in range(len(x)):
        if i > 5 and i <10:
            f = f + x[i]
    return f"""
    

##########
# DESCRIPTION
#	Takes each image and adds exp_Time's return value to the list exp.
# PARAMETERS	
#	images - list of fits files
#	exp - a list of exposure times
# RETURNS
#	list of exposure times
##########
def exp_List_build(images):
    exp = []
    for i in images:
        exp.append(exp_Time(i))
    return exp

##########
# DESCRIPTION
#	Opens a fits header, takes the exposure time and returns it.
# PARAMETERS
#	x - input file
#	hdulist - image information
#	head - the header
#	t - the exposure time
# RETURN
#	exposure time
##########		
def exp_Time(x):
    hdulist = fits.open(x)
    head = hdulist[0].header
    if 'EXPTIME' in head.keys():    
        t = head ['EXPTIME']
        hdulist.close()
    else:
        t = "None"
    hdulist.close()
    return t 


##########
# DESCRIPTION
#	Takes each image and adds date_Time's return value to the list time.
# PARAMETERS	
#	images - list of fits files
#	time - a list of times when the images were taken
# RETURNS
#	list of times/dates
##########    
def date_build(images):
    time = []
    for i in images:
        time.append(date_Time(i))
    return time


##########
# DESCRIPTION
#	Opens a fits header, takes the time the image was taken and returns it.
# PARAMETERS
#	x - input file
#	hdulist - opens the image information
#	head - the header
#	d - the time when the image was taken
# RETURN
#	time an image was taken
##########
def date_Time(x):
    hdulist = fits.open(x)
    head = hdulist[0].header
    if 'DATE-OBS' in head.keys():    
        d = head ['DATE-OBS']
        hdulist.close()
    else:
        d = "None"
    hdulist.close()
    return d	


##########
# DESCRIPTION
#	Takes each image and adds color's return value to the list filter.
# PARAMETERS	
#	images - list of fits files
#	filter - a list of objects observed
# RETURNS
#	filter
##########
def color_build(images):
    filter = []
    for i in images:
	    filter.append(color(i))
    return filter
		

##########
# DESCRIPTION
#	Opens a fits header, takes the object and returns it.
# PARAMETERS
#	x - input file
#	hdulist - image information
#	head - the header
#	f - the object
# RETURN
#	object observed and through what filter if there was one
##########
def color(x):
    hdulist = fits.open(x)
    head = hdulist[0].header	
    if 'OBJECT' in head.keys():    
        f = head ['OBJECT']
        hdulist.close()
    else:
        f = "None"
    hdulist.close()
    return f
    

##########
# DESCRIPTION
#   builds a list called foc that contains the focus string from the header
# PARAMETERS
#   foc - list of focus strings
# RETURNS
#   foc - retruns list to file()
##########
def Focus_build(images):
    foc = []
    for i in images:
        foc.append(focus(i))
    return foc

##########
# DESCRIPTION
#	Opens a fits header, takes the focus and returns it.
# PARAMETERS
#	x - input file
#	hdulist - image information
#	head - the header
#	fo - the focus
# RETURN
#	fo - the focus returns to focus_build()
##########		
def focus(x):
    hdulist = fits.open(x)
    head = hdulist[0].header
    if 'FILTER' in head.keys():    
        fo = head ['FILTER']
        hdulist.close()
    else:
        fo = "None"
    hdulist.close()
    return fo
    
    
if __name__=='__main__': main() 
