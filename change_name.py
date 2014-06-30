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
#	Starts at base_path and calls functions to create a list of images, then
#     a list of dates, then a list of filenumbers. It then gets the most frequently 
#     occuring date from UT time in the header. Loops through images and num through 
#     the length of images, which is the same as the length of dates and num. 
# PARAMETERS
#	base_path - where you want the program to start running
#	images    - the fits files in the current path
#	dates     - list of dates in the header.
#     date1     - most frequently occuring date in the headers in the directory
#     num       - list of filenumbers
# RETURNS
#	nothing
##########

def main():
    base_path = 'C:\Users\Maria\.spyder2\mar30_14'
    #base_path = "/nfs/home/observatory/data/scheduler"
    os.chdir(base_path)
    print os.getcwd()
    files = os.listdir(base_path)     
    images = sort(files)
    # list of month and day date strings
    dates = date_build(images)
    # list of filenumbers - fixed if the date changes in the header then 1000 is
    # added to the filenumber
    num = change_filenumber(dates,images)
    # single most occuring date in the list of files    
    date1 = mode_date(dates)
    for i in num:
        print (date1 + "_" + i)
    for k in range(len(images)):  
        f1 = fits.open(images[k])
        #puts the cooresponding header into the new file
        hdu = fits.PrimaryHDU(f1[1].data,f1[0].header)
        hdulist = fits.HDUList(hdu)
        #creates the new file name
        hdulist.writeto(date1 + "_" + num[k] + ".fits")
                        
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
#    Loops through the list dates and finds the most frequently occuring date
#    by comparing each date to all the other dates. Then picks out the first 3 
#    characters of the date and changes the month from a numerical representation
#    to word form.
# PARAMETERS
#    largest - the largest count for the dates so far.
#    cnt     - keeps track of the current strings occurance
#    the_mode- the mode date
#    l       - the constructed day string
#    p       - the constructed month string
#    w       - month and day string
# RETURNS
#    w       - returns the month and day string back to main and sets it equal
#              to date1.
###########
def mode_date(dates):
    largest =0
    for j in dates:
        for o in range(len(dates)):
            cnt =0
        for u in dates:
            for e in range(len(dates)):
                if dates[o] == dates[e]:
                    cnt = cnt + 1
    if cnt> largest:
        largest = cnt
        the_mode = dates[o]
        p =""
        l =""
        w =""
        for k in range(len(the_mode)):
            # gets day
            if k >2:
                l = l + the_mode[k]
            #gets month
            if k>= 0 and k<3:
                p = p + the_mode[k]
                if p == "01-":
                    p = "Jan"
                if p == "02-":
                    p = "Feb"
                if p == "03-":
                    p = "Mar"
                if p == "04-":
                    p = "Apr"
                if p == "05-":
                    p = "May"
                if p == "06-":
                    p = "Jun"
                if p == "07-":
                    p = "Jul"
                if p == "08-":
                    p = "Aug"
                if p == "09-":
                    p = "Sep"
                if p == "10-":
                    p = "Oct"
                if p == "11-":
                    p = "Nov"
                if p == "12-":
                    p = "Dec"
    #combines the new month string with the day               
    w = p + l                   
    print w
    return w


##########
# DESCRIPTION
#   Picks out the date strings in the list dates. Compares all dates to the first 
#   date in the list. If the date string doesn't match the first one, then the 
#   date changed in the header. Calls counter which will add 1000 to the filenumber
#   if the strings match, filename is called and picks out the original filenumber.
# PARAMETERS
#   sdata     - the start date in the files
#   filenumber- the new filenumber after counter has changed it.
# RETURNS
#   num       - returns the list of filenumbers back to main and is set equal to num
###########
def change_filenumber(dates,images):  
    sdate = dates[0]
    print images
    num = []
    for i in range(len(dates)):
        if sdate != dates[i]:
            n = counter(images[i])
            # adds to the list num
            num.append(n)
        else:
            n = filename(images[i])
            # adds to the list num
            num.append(n)
    return num


##########
# DESCRITPION
#   Loops through the original filename string and picks out the filenumber.
# PARAMETERS
#   f  - the constructed filenumber
# RETURNS
#   f  - returns the filenumber to either change_filenumber or counter
##########                
def filename(x):    
    f =""
    for j in range(len(x)):
        if j > 5 and j <10:
            f = f + x[j]
    return f


##########
# DESCRIPTION
#   Loops through images and calls a function to loop through the date stings
#   in the headers and adds them to the list dates.
# PARAMETERS
#   dates - list of date strings
# RETURNS
#   dates - returns the list of dates to main
##########    
def date_build(images):
    dates = []
    for i in images:
        dates.append(date_Time(i))
    
    return dates


##########
# DESCRIPTION
#   Picks the date string off of the header and only picks out the month and 
#   date by looping through each date string.
# PARAMETERS
#   hdulist - opened fits file
#   head    - fits header
#   d       - the string contained in the the date observed header card
#   t       - only the month and day part of the date string
# RETURNS
#   t       - returns the month and day string back to date build
###########
def date_Time(x):
    hdulist = fits.open(x)
    head = hdulist[0].header
    d = head['DATE-OBS']
    hdulist.close()
    for i in d:
       t =""
       for j in range(len(d)):
           #gets month and day string
           if j > 4 and j <10:
               t = t + d[j]
    #print t
    return t


##########
# DESCRIPTION
#   gets the filenumber from the funciton filename. converts it to an integer.
#   adds 1000 and returns it back to a string.
# PARAMETERS
#   filenum - 4 character filenumber from filename
#   n       - integer conversion of the number string
#   xnum    - number plus 1000
#   fixnum  - the fixed filenumber in string form.
# RETURNS
#   fixnum  - returns the fixed filenumber back to change_filenumber
########## 
def counter(string):
    filnum = filename(string)
    n = int(filnum)
    xnum = n + 1000
    fixnum = str(xnum)
    return fixnum
 
if __name__=='__main__': main()    