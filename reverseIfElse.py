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
	return re.finditer(r"if\s*\((.+\))\s*\{\s*\}\s*else\s*\{((\{.*\}|[^{$}])*)\}", searchStr)
	


#def getElseBodyPart():

#def getIfExpression():

#def negateExpression():

#def switchIfBodyWithElseBody():

#def readAllFilesFromFolder(folder):

def main():
	fileName = "d:\Views\evoSiSz0_ESF_CoreDev_002.001_AT_pre\ESF_CORE\dev\logic\src\BaseSI.cpp"
	fileContents = getFileContents(fileName)
	matches = findIfWithEmptyBodyInString(fileContents)
	for m in matches:
		print 'IF Expression: %s \n +++++++ \n ELSE Contents: \n %s \n --------' % (m.group(1), m.group(2))
		print 'start: %d end: %d' % (m.start(1), m.end(1))



if __name__ == "__main__":
	main()