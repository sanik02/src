# The following code can read our CSV files, looking for side effect name and mapping them to STITCH id's.
# The next step (which hasn't been completed) is to go back to our SIDER document, and write in a new column for names.
# Once we have common names, we can easily modify our prototype in order to map side effects onto common names.

# The following code, written on 6/9/16 and 6/10/16 creates a dictionary of two chosen attributes from a CSV.
# I've been using a file called TestCSV (a subset of SIDERcsv) for testing my code.
# So far, I can create key value pairs of side effects to arrays of drugs.
# All the side effects are unique.  The next step is to delete duplicates of drugs WITHIN these arrays.
# This can easily be done with the set() function (I THINK).  More testing to be done later.

import csv
import os
import pandas


def filechecking():
    if os.path.exists("./TESTcsv.csv"):
        print('The file exists!')
    else:
        print('Sorry, cannot find the file you want to read from.  Check the path carefully!')
        return 0


def readfile():
    # create a blank dictionary
    dictionary = {}

    # Upon creating our dictionary, we will have made many duplicates of drugs.  So now we should delete the excess.
    # To do this, we go through each key in the dictionary and use the set() function to get rid of duplicates.
    # The trim function only works if there is more than one element (in order to avoid splitting strings into chars).

    def trim():
        for key in dictionary:
            if not (isinstance(dictionary.get(key), basestring)):
                originalarray = dictionary.get(key)  # obtain the array.
                newarray = list(set(originalarray))  # remove all duplicate drug entries.
                dictionary.update({key: newarray})  # update the entry in the dictionary.
            else:
                dictionary[key] = [dictionary[key]]

    # This function starts reading from our file into our dictionary.
    def scan():
        with open("./TESTcsv.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                sidefx = row[5]
                drugid = row[0]
                if sidefx in dictionary:
                    # find the key in the dictionary, and get the array
                    # if there is only one value, we'll have to make an array with the old value and the new value
                    # but if there are at least two values, appending to the array shouldn't be hard at all

                    # if there is only one value then dictionary.get(sidefx) will be a string. The next lines test for this.
                    if isinstance(dictionary.get(sidefx), basestring):
                        # get first value
                        first = dictionary.get(sidefx)
                        # create an array with first value and second value
                        array1 = [first, drugid]
                        # update key to have this array
                        dictionary.update({sidefx: array1})
                    # if there are two or more values, then each key of the dictionary will hash to an array
                    else:
                        # get value (should be in the form of an array)
                        array2 = dictionary.get(sidefx)
                        # append drug id to the array
                        array2.append(drugid)
                        # update key to have this array
                        dictionary.update({sidefx: array2})
                else:
                    # create a new side effect Key value pair
                    dictionary.update({sidefx: drugid})
    scan()
    trim()
    print dictionary


filechecking()
readfile()