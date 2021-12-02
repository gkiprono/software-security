###########################################################
#GABRIEL KIPRONO
#WORKSHOP 3
#parser.py
#September 18 2021
############################################################

from ast import Str
from sre_constants import error
import yaml
import os
import re
import sys
import numpy as np

from yaml import loader

#list of all insecure variables and code smells
insecureVariables = []

#classifications of security weaknesses
securityClassification = {1:"Admin by default", 2:"Empty passwords", 3:"Hard coded secret",
						   4:"Missing default in case statement", 5:"No integrity check", 6:"Suspicious commmnet",
						   7:"Unrestricted Ip address", 8:"Use of HTTP without SSL/TLS", 9:"Use of weak cryptography algorithms"}

fileName = "Workshop3.values.yaml"
fileNameB = "Workshop3.play1.yaml"
fileNameC = "Workshop3.play2.yaml"

class SecurityWeakness:
	name = ""
	keyword = {}

	def __init__(self, name, keys):
		self.name = name
		self.keyword = keys



def parse(yamlFile):
	with open(yamlFile) as stream:
		try:
			print()
			dict = yaml.load(stream, Loader=yaml.FullLoader)
			print(dict)
		except yaml.YAMLError as exc:
			print(exc)

	return dict
			

def parseAll(yamlFile):
	with open(yamlFile) as ymfile:
		contents = yaml.load_all(ymfile, Loader=yaml.FullLoader)
		for content in contents:
			for elementA, elementB in content.items():
				print(elementA, ":", elementB)
	
	return contents
					
					
def checkOccurance(securityWeakness, yamlFile):
	lineNumber = 1
	with open(yamlFile) as ymFile:
		contents = yaml.load_all(ymFile, Loader=yaml.FullLoader)
		for content in contents:
			for variable, value in content.items():
				for weakness in securityWeakness.keyword:
					variableFound = re.search(weakness, str(value))
					valueFound = re.search(weakness, str(variable))
					if(valueFound or variableFound):
						variableViolation = variable
						print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
						print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
						print("Security weakness name: ",securityWeakness.name)
						print("Security weakness location:", findLineNumber(yamlFile, variableViolation), " " , variableViolation)
						searchString(fileNameB, variableViolation)
						searchString(fileNameC, variableViolation)
						if variableViolation not in insecureVariables:
							insecureVariables.append(variableViolation)

			

def findLineNumber(fileName, word):
	lineNum=0
	resultsList = []
	with open(fileName, 'r') as infile:
		for line in infile:
			lineNum = lineNum+1
			if word in line:
				resultsList.append(lineNum)

	return resultsList


def searchString(fileName, word):
	lineNum=0
	resultsList=[]
	with open(fileName, 'r') as file:
		for line in file:
			lineNum = lineNum+1
			if word in line:
				resultsList.append((lineNum, line.rstrip()))
				print("Security weakness usage line: ",lineNum, " play name ",line.strip(), " in file ", fileName)


def readFile(dictionary):
	for index, key in enumerate(dictionary):
		print(index,key)

def main():
	#check yamlContents for following flags/weaknesses
	#I found the following instances by performinf dry-run
	adminByDefault = SecurityWeakness(securityClassification.get(1), {"admin","user=>'admin"})
	hardCodedSecret = SecurityWeakness(securityClassification.get(3), {"sat_user", "sat_pass","sat_email"})
	emptyPasswords = SecurityWeakness(securityClassification.get(2), {"passwd=''"})
	missingDefCase = SecurityWeakness(securityClassification.get(4), {})
	noIntegrityCheck = SecurityWeakness(securityClassification.get(5), {".tar",".gz",".zip",".dmg",".tar",".tgz",".rpm","tar.gz"})
	suspiciousComment = SecurityWeakness(securityClassification.get(6), {"HACK", "FIXME", "TODO"})
	unrestrictedIP = SecurityWeakness(securityClassification.get(7), {"0.0.0.0"})
	useofHTTPWithoutSSL = SecurityWeakness(securityClassification.get(8),{"http://"})
	weakCryptoAlgorithms = SecurityWeakness(securityClassification.get(9), {"MD5","SHA-1"})

	#collect all insecure instances store in insecureVariables list
	checkOccurance(adminByDefault, fileName)
	checkOccurance(hardCodedSecret, fileName)
	checkOccurance(noIntegrityCheck, fileName)
	checkOccurance(suspiciousComment, fileName)
	checkOccurance(unrestrictedIP, fileName)
	checkOccurance(useofHTTPWithoutSSL, fileName)
	checkOccurance(weakCryptoAlgorithms, fileName)



	

if __name__ == "__main__":
	main()