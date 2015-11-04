__author__ = 'Sebastien Robitaille'

class standardValueDataWraper:

    def __init__ (self):
        print("creating SVD wraper class")

    valueID = None #
    valueName = None
    value = None
    valueType = None
    valueUnit = None

    dateAdded = None #
    dateUpdated = None #

    containingFileID = None
    sourceLocation = None
    sourceParser = None

    catagory = None
    tags = None
    commonName = None
    location = None
    descriptionShort = None
    description = None
    otherData = None

    def parseXML (self, input):
        #parser XML from input

    def writeXML (self, outputFile):
        #write class data to file


class standardValueDataInport:

    def __init__(self, valueName, value, valueType):
        data = standardValueDataWraper()




class standardValueDataExport:

    def __init__(self):
        data = standardValueDataWraper()











    
