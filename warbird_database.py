# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:38:19 2021

@author: mars2699
"""

# Locate the data file
import sys
foldername = 'c:\\MA305\\'
filename = foldername + 'warbird_data.txt'
import math
try:
    f_in = open(filename, 'r')
except FileNotFoundError:
    print('File %s DOES NOT exist.\n File must exist to proceed...exiting.\n' % filename)
    sys.exit('failed on opening input file %s ' % filename)
    
line = f_in.readline()
lc = 0
while line:
    line = line[:-1]
    lc += 1
    print('line %2d: %s' % (lc, line))
    if lc == 29:
        break
    line = f_in.readline()
   
f_in.seek(0)   

# Print a welcome message to the user, as well as state the categories
userSelection = input('Welcome to the Warbird Database! Which category would you like to explore? Enter 1 for fighters, 2 for reconnaissance, 3 for bombers, 4 for jets, or 5 for transports: ')
userSelection = int(userSelection)

# Establish a column to each category
values = []
line = f_in.readline()
lc = 0
while line:
    lc = lc + 1
    if lc == 1:
        line = f_in.readline()   
        next
f_in.close()

# Show appropriate column/category to user

# Ask user which Warbird they would like to select

# Ask user if they wish to read the Wikipedia article on the aircraft, 
# look at photos of it, or watch a video about it

# Establish links to Wikipedia sites

# Establish links to Google images results

# Establish YouTube links

# Create a message in case of no available YouTube videos
