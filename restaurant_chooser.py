#!/usr/bin/env python3.4 
#
# Lunch Generator AKA Restaurant Chooser
# Let the machine do the deciding
#
# v0.0
# 24 apr 2018 rkeepers 
##################################################

# lets import a bunch of libraries cause thats how i roll
import random
import os
import csv
import sys
#import datetime
def main():
    restDictionary = {}
    # count the number of restuarnts in the list
    # ( ugh! ) "rest" will do cause I can't spell
    # count the number of rest in the list
    count = 0

    # read list of restaurants from file
    #open the file and iterate line by line into the dictionary
    fileName = csv.reader(open('restaurantData.dat', 'rU'), delimiter=',')
    for line in fileName:
        count += 1
        # put them into a dictionary
        restDictionary[count] = line



    # generate a random number between range
    # start with 3 to skip the RestaurantData.dat header lines
    randomNumber = random.randint(4, count)

    # correlate the number with the correct rest
    result = restDictionary[randomNumber]
    # display result
    print("The restaurant for today is: ", result[0])

    # reject, rate, and re-generate
    # query user to accept, quit or try again(skip)
    # toDo: we will add a count to that rest's scorecard
    # or perhaps write the output to a logfile that can
    # be harvested later...
    #

    # at some point, exit 0
    SystemExit(0)
    
if __name__ == '__main__':
  main()    
