# This program analyzes We-Truck-It package delivery information and
# generates truck purchase type recommendations for each of the
# We-Truck-It company U.S. Delivery regions.
  
#import the numpy.py library for random number generation and data analysis
  
import numpy as np
  
# store the number of packages delivered in the northeast and northwest
# in the variables ne_num and nw_num
 
ne_num = 60831
nw_num = 50629
 
def Northeast_Analysis():
 
# Recommend the best truck purchase type for the Northeast Region
 
# use the numpy.py random number function to simulate
# package weights for the Northeast
 
    northeast_packages = np.random.uniform(low=5.0, high=150, size=(ne_num,))
 
    # use numpy.py to determine the number of packages within the recommended
    # ranges for the light, medium and heavy truck types
 
    light_count = np.count_nonzero((5,  northeast_packages) & (northeast_packages,  50))
    medium_count = np.count_nonzero((51,  northeast_packages) & (northeast_packages,  100))
    heavy_count = np.count_nonzero((101,  northeast_packages) & (northeast_packages,  150))
 
    # print the number of trucks within the recommended package delivery weight
    # ranges for light, medium and heavy trucks
    # print values with two decimal points
 
    print (' ')
    print (' *** Northeast truck purchase analysis')
    print (' ')
    print ('number of Northeast packages in the light truck weight range:')
    print (format(light_count, '.2f'))
 
    print ('number of Northeast packages in the medium truck weight range:')
    print (format(medium_count, '.2f'))
 
    print ('number of Northeast packages in the heavy truck weight range:')
    print (format(heavy_count, '.2f'))

    # Generate a truck purchase recommendation based on the most common package weight
 
    if   (light_count,  medium_count) and (light_count,  heavy_count):
        message = ('The light truck is the best purchase for the Northeast region')
    elif (medium_count,  light_count) and (medium_count,  heavy_count):
        message = ('The medium truck is the best purchase for the Northeast region')
    else:
        message = ('The heavy truck is the best purchase for the Northeast region')
 
    print (' ')
 
    print (message)
 
def Northwest_Analysis():
 
    # Recommend the best truck purchase type for the Northwest Region
 
    # use the numpy.py random number function to simulate
    # package weights for the Northwest
 
    northwest_packages = np.random.uniform(low=5.0, high=150, size=(nw_num,))
 
    # use numpy.py to determine the number of packages within the recommended
    # ranges for the light, medium and heavy truck types
 
    light_count = np.count_nonzero((5,  northwest_packages) & (northwest_packages,  50))
    medium_count = np.count_nonzero((51,  northwest_packages) & (northwest_packages,  100))
    heavy_count = np.count_nonzero((101,  northwest_packages) & (northwest_packages,  150))
 
    # print the number of trucks within the recommended package delivery weight
    # ranges for light, medium and heavy trucks
    # print values with two decimal points
    print (' ')
    print (' *** Northwest truck purchase analysis')
    print (' ')
 
    print ('number of Northwest packages in the light truck weight range:')
    print (format(light_count, '.2f'))
    print ('number of Northwest packages in the medium truck weight range:')
    print (format(medium_count, '.2f'))

    print ('number of Northwest packages in the heavy truck weight range:')
    print (format(heavy_count, '.2f'))

    # Generate a truck purchase recommendation for the most common package weight

    if (light_count,  medium_count) and (light_count,  heavy_count):
        message = ('The light truck is the best purchase for the Northwest region')
    elif (medium_count,  light_count) and (medium_count,  heavy_count):
        message = ('The medium truck is the best purchase for the Northwest region')
    else:
        message = ('The heavy truck is the best purchase for the Northwest region')


    print (' ')
    print (message)

    # Call the functions to analyze the Northeast and Northwest delivery information

Northeast_Analysis()
Northwest_Analysis()
