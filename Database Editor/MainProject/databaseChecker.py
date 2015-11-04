__author__ = 'Sebastien Robitaille'
import os
import time

import parser_Metadata

#metadata file format
#
#title(databaseMetadata)
#date/time created
#database version
#

databaseFolderName = "World_Map_Database" #the name of the folder containing the database
databaseMetaDataFileName = "databaseMeta.meta" #name of the database metadata file
databaseVersion = "A0.1" #current database verseion (A = alpha B = bata)

def checkdatabase (programmeBasePath): #folder containing database folder
    print("Checking Database")
    print("Checking for Database Folder")

    databaseFolderPath = programmeBasePath+"/"+databaseFolderName #create database folder path from programe path and database folder name
    print(databaseFolderPath)
    databaseFolderFound = (os.path.exists(databaseFolderPath)) #check if database folder path exists

    if databaseFolderFound: #check if database folder was found
        print("Database Folder Found")
    else:
        print("Database Folder Not Found")
        print("Creating Database Folder")
        os.mkdir(databaseFolderPath) #if not create database folder

    print("Checking Database metadata file")

    databaseMetaDataFilePath = databaseFolderPath+"/"+databaseMetaDataFileName #create database metadata folder path from database folder path and database meatadata folder name
    print (databaseMetaDataFilePath)
    databaseMetaDataFileFound = os.path.exists(databaseMetaDataFilePath) #check if metadata file exists
    if databaseMetaDataFileFound: #check if metadata file was found
        print("Database Metadata File Found")
    else:
        print("Database Metadata File Not Found")
        print("Creating Database Metadata File")
        createDatabaseMetadataFile(databaseMetaDataFilePath) #if not create file

    print("Parsing Metadata File")
    databaseMetaData = parser_Metadata.parseFile(databaseMetaDataFilePath)#parse metadata file
    if(databaseMetaData['Title'] != "databaseMetadata"): #check if title is valid
        print("File Invalid")
    else:
        version = databaseMetaData['DatabaseVersion'] #save version
        createdOn = databaseMetaData['CreatedOn'] #save date created

        print("Databas Version: "+version)
        print("Created On: "+createdOn)

def createDatabaseMetadataFile(filePath):

    metaDataFile = open(filePath,'w')#open file
    metaDataFile.write("Title=databaseMetadata=\n") #write title to file
    currentTime = time.strftime("%I:%M:%S")#get current time
    currentDate = time.strftime("%d:%m:%Y")#and data
    metaDataFile.write("CreatedOn="+currentDate+":"+currentTime+"=\n")#write date and time ti file
    metaDataFile.write("DatabaseVersion="+databaseVersion)#write database version to file
    metaDataFile.close()#close file
