# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Maria\.spyder2\.temp.py
"""


#####Take out hard coding of key words and make them arguments#######



from astropy.io import fits
import os

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
    base_path = 'C:\Users\Maria\Physics_Research\Originals_Renamed'
    os.chdir(base_path)
    print os.getcwd()
    files = os.listdir(base_path)    
    images = sort(files)
    file(images,"catalog.txt")
            
            
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
    filters = color_build(images)
    names = name_build(images)
    exp = exp_List_build(images)
    air = Airmass_build(images)
    foc = Focus_build(images)    
    time = date_build(images)
    if os.path.exists(filename):
        os.remove(filename)
    # creates a new catalog and puts into the variable info
    info = open(filename, "w")
    info.write("%10s,%15s,%15s,%20s,%15s,%10s,%30s,%10s\n" % ("Filenumber","Name","Filter","Exposure Time","Air Mass","Focus","Time Taken","Comments"))    
    # wirtes information from lists into files
    for i in range(len(images)):
        info.write('%10s,' % filenum[i])
        info.write('%15s' % names[i])
        info.write('%15s' % filters[i])
        info.write('%20s,' % exp[i])        
        info.write('%15s,' % air[i])        
        info.write('%13s,' % foc[i])
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
    filters = []
    for i in images:
	    filters.append(color(i))
    return filters
		

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
    if 'FILTER' in head.keys():    
        f = head ['FILTER']
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
    if 'FOCUS' in head.keys():    
        fo = head ['FOCUS']
        hdulist.close()
    else:
        fo = "None"
    hdulist.close()
    return fo
    
    
##########
# DESCRIPTION
#   builds a list called air that contains the airmass string from the header
# PARAMETERS
#   air - list of air mass strings 
# RETURNS
#   air - retruns list to file()
##########
def Airmass_build(images):
    air = []
    for i in images:
        air.append(airmass(i))
    return air

##########
# DESCRIPTION
#	Opens a fits header, takes the airmass and returns it.
# PARAMETERS
#	x - input file
#	hdulist - image information
#	head - the header
#	a - the airmass
# RETURN
#	a - returns the airmass to Airmass_build()
##########
def airmass(x):
    hdulist = fits.open(x)
    head = hdulist[0].header
    if 'AIRMASS' in head.keys():    
        a = head ['AIRMASS']
        hdulist.close()
    else:
        a = "None"
    hdulist.close()
    return a 
	
##########
# DESCRIPTION
#	Takes each image and adds color's return value to the list filter.
# PARAMETERS	
#	images - list of fits files
#	filter - a list of objects observed
# RETURNS
#	filter
##########
def name_build(images):
    names = []
    for i in images:
	    names.append(color(i))
    return names
		

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
def name(x):
    hdulist = fits.open(x)
    head = hdulist[0].header	
    if 'OBJECT' in head.keys():    
        n = head ['OBJECT']
        hdulist.close()
    else:
        n = "None"
    hdulist.close()
    return n  
    
if __name__=='__main__': main() 
