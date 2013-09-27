import re

def getFileContents(fileName):
	f = open(fileName, "r")
	fileContents = f.read()
	f.close()
	return fileContents

def findIfWithEmptyBodyInString(searchStr):
	prog = re.compile(r'\{$.*?^\}$', re.DOTALL | re.MULTILINE)
	return prog.finditer(searchStr)

def findNestedString(searchStr):
	matches = re.finditer(r'if((:?.*?\s*)*)\{\s*\}', searchStr)
	expressions = []

	for m in matches:
		first = m.group().find('(') # first occurrence of '('
		last = m.group().rfind(')') # find last occurrence of ')'
		if first == -1 or last == -1:
			raise NameError("Invalid searchStr! There are missing brackets!")
		expressions.append(m.group()[first+1 : last])

	return expressions

#def getElseBodyPart():

#def getIfExpression():

#def negateExpression():

#def switchIfBodyWithElseBody():

#def readAllFilesFromFolder(folder):

def main():
	fileName = "d:\Views\evoSiSz0_ESF_CoreDev_002.001_AT_pre\ESF_CORE\dev\logic\src\BaseSI.cpp"
	expressions = findNestedString(getFileContents(fileName))
	print expressions
	
if __name__ == "__main__":
	main()