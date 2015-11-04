__author__ = 'Sebastien Robitaille'

#file format
#
#<title>=<value>
#

def parseFile(filePath):
    file = open(filePath, 'r') #open file in read mode
    output = {} #output dictionary
    loop = True #loop var

    while loop: #while lopp is true
        line = file.readline() #read next line
        if line == "": #check if line is blank
            loop = False #exit lopp
        else: #if line is not blank
            lineSplit = line.split("=") #split line on =
            output[lineSplit[0]] = lineSplit[1] #add value name and value to the dictionary

    print(output)
    return output #return dictionary








