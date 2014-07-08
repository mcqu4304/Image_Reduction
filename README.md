Image_Reduction
===============

Files to manipulate fits files and reduce image data

Scripts:
	Check_headers
		creates a text catalog to check if the 		object names match the 		appropriate filters
	Color_filename
		uses the filter information in the 		header to add the filter to the front 		of the filename for easy recognition.
	cat_creator
		creates a text catolog with header 		information of all images in a 		directory.
	change_name
		changes the original filename to a 		easier to read name with the month day 		and filenumber of the image.
	filter_interp
		reads filter wheel information and 		adds a filter color in english as a 		filter card.
	fits_functions
		multiple functions to manipulate fits 		files. 
		which include:
			open_fits
			change_header
			append_header
			image_subtraction
			image_division
			std_of_plv
			normalize
			new_headercard
			data_plot
	image_manipuation
		utilizes functions from fits_funcitons 		to perform them on multiple images.
	mask_creator
		creates a boolean mask of the image 		and then negates the image.
	median_image
		takes a list of images and creates a 		median image.
	overscan
		takes the overscan on a 4150 by 4150 		image and finds the median overscan 		value and subtracts it from the 		cooresponding image.
	pixel_extract - main branch
		finds the median sky for a combined 		image.
	pixel_extract - sky branch
		finds the median sky value and 		subtracts it from the corresponding 		image.