'''
Gabriel Kiprono
CSC 4585-
Workshop 5

'''

import javalang
from javalang import util
import javalang.tokenizer as tokenizer
import os
import fnmatch
import xml
import glob
import tokenize
import xml.etree.ElementTree as ET
import pandas as pd
from pathlib import Path

permissions = pd.DataFrame()

results = pd.DataFrame(columns=['full path', 'line','permission'])


def readJavaFile(directory):
    srcFile = open(directory, encoding='UTF8')
    srcCode = srcFile.read()
    srcFile.close()

    return srcCode

##########################################3
#Checks contents of java file for permission use
#
#
##########################################

def checkForPermissionRequests(src, perms,dir):
    no=1
    useperms = False
    srcList = src.splitlines()
    for line in srcList:
        
        for permission in perms.name:
            if permission in line:
                useperms = True
                results.loc[-1] = (dir,no,permission)
                results.index+=1

        no+=1

    

##############################
#parse provided xml file
#
##############################

def xmlParser(filePath):
    permissions = []
    try:
        xmlFile = open(os.path.join(os.path.dirname(__file__), filePath), 'r')
        xmlCode = ET.parse(xmlFile)
        root = xmlCode.getroot()
        for permission in root.iter('uses-permission'):
            #print(permission.attrib.get('{http://schemas.android.com/apk/res/android}name'))
            permissions.append(permission.attrib.get('{http://schemas.android.com/apk/res/android}name'))

        permissionsDF = pd.DataFrame(permissions, columns=['Permission'])   
        return permissionsDF

    except xml.etree.ElementTree.ParseError as e:
        pass


#########################
#CSV containing the dangerous permissions
#
#########################
def readCsv():
    dangerousPermissions = pd.read_csv("dangerousPermissions.csv")
    #print(dangerousPermissions)
    return dangerousPermissions

############################
#Takes rootfolder of the project and parses all files to get java files only
#
#
############################
def exploreForJava(rootFolder,perms):
    javaTemplate = ".java"
    for root,dir,files in os.walk(rootFolder, topdown=False):
        for name in files:
            if javaTemplate in name:
                javaFile = os.path.join(root, name)
                srcCode = readJavaFile(javaFile)
                checkForPermissionRequests(srcCode, perms,javaFile)
        #print(files)


def main():
    xmlTemplate = "AndroidManifest.xml"
    permissions = readCsv()
    
    #all android apps src folder
    rootFolder = r"C:\Gabriel\School\Coursework\Fall 21\\4585\Workshops\Android permissions\FARMING_ANDROID_REPOS"

    try:
        for root, dir, files in os.walk(rootFolder, topdown=False):
            
            for name in files:
                #get all xml files, note the directory
                a=0
                if fnmatch.fnmatch(name, xmlTemplate):
                    

                    xmlFile = os.path.join(root, name)
                    xmlPermissions = xmlParser(xmlFile)
                    riskyPermissions = xmlPermissions.merge(permissions,on=['Permission'])
                    if not riskyPermissions.size == 0:
                        exploreForJava(root,riskyPermissions)

    except OSError as e:
        print(e)

    finalDf = results.sort_index()
    finalDf.to_csv("Workshop#5_Output.csv")
    print("output in Workshop#5_Output.csv")

    print(finalDf.head(5))


if __name__ == "__main__":
    main()
