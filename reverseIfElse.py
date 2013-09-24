import re

def getFileContents(fileName):
	f = open(fileName, "r")
	fileContents = f.read()
	f.close()
	return fileContents

# group 0 - all matched
# group 1 - expression inside if
# group 2 - everything inside the else between the braces {...}
def findIfWithEmptyBodyInString(searchStr):
	for m in re.finditer(r"if\s*\((.+\))\s*\{\s*\}\s*else\s*\{((\{.*\}|[^{$}])*)\}", searchStr):
		print 'IF Expression: %s \n +++++++ \n ELSE Contents: \n %s \n --------' % (m.group(1), m.group(2))

#def getElseBodyPart():

#def getIfExpression():

#def negateExpression():

#def switchIfBodyWithElseBody():

#def readAllFilesFromFolder(folder):

def main():
	fileContents = getFileContents("d:\Views\evoSiSz0_ESF_CoreDev_002.001_AT_pre\ESF_CORE\dev\logic\src\BaseSI.cpp")
	findIfWithEmptyBodyInString(fileContents)

if __name__ == "__main__":
	main()