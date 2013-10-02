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

def findMinimal(searchStr):

	prog = re.compile(r'\{\s*\}\s*else\s*\{', re.DOTALL)
	matches = prog.finditer(searchStr)
	
	posInSearchStr = 0

	ifExpressions = []
	elseBlocks = []
	matchObjects = []

	for m in matches:

		matchObjects.append(m)

		# find else block
		openCurlyBraceCount = 1
		posInSearchStr = m.end()

		elseBlock = ""
		while openCurlyBraceCount != 0:
			curChar = searchStr[posInSearchStr]
			if curChar == '{':
				openCurlyBraceCount += 1
			if curChar == '}':
				openCurlyBraceCount -= 1

			if openCurlyBraceCount == 0:
				break

			elseBlock += curChar
			posInSearchStr += 1

		elseBlocks.append(elseBlock)


		# find if expression
		openBraketCount = 1
		posInSearchStr = m.start()

		while curChar != ')': # !!!WEAKNESS: Error when searchStr contains invalid expression!
			curChar = searchStr[posInSearchStr]
			posInSearchStr -= 1

		ifExpression = ""
		while openBraketCount != 0:
			curChar = searchStr[posInSearchStr]
			
			if curChar == ')':
				openBraketCount += 1
			if curChar == '(':
				openBraketCount -= 1

			if openBraketCount == 0:
				break

			ifExpression += curChar
			posInSearchStr -= 1

		ifExpressions.append(ifExpression[::-1])

	return matchObjects, ifExpressions, elseBlocks

def insertRevStart(author, insertPos):
	revStart = "// @revstart[-] 20130926 " + author + " replace else query by a negated if query"


def insertRevEnd(author, insertPos):
	revEnd = "// @revend 20130926 " + author

def determineIndentationOfRevStartCommentFromPos(ifExprStartPos, searchStr):
	posInSearchStr = ifExprStartPos
	indentation = ""
	curChar = ''
	while curChar != '\n' and posInSearchStr >= 0:
		curChar = searchStr[posInSearchStr]
		indentation += curChar
		posInSearchStr -= 1

	indentation = indentation[::-1] # reverse
	try:
		indentation = indentation[:indentation.index('if')]
	except Exception, e:
		raise Exception("Invalid IF expression!")

	return indentation

def insertElseIntoIf(searchStr):
	matches, ifs, elses = findMinimal(searchStr)

	result = searchStr

	for m in reversed(matches):
		result = result[:m.start()+1] + result[m.end():]

	return result

#def getElseBodyPart():

#def getIfExpression():

#def negateExpression():

#def switchIfBodyWithElseBody():

#def readAllFilesFromFolder(folder):

def main():
	#fileName = "d:\Views\evoSiSz0_ESF_CoreDev_002.001_AT_pre\ESF_CORE\dev\logic\src\BaseSI.cpp"
	fileName = "test.txt"
	expressions = findNestedString(getFileContents(fileName))
	print expressions

if __name__ == "__main__":
	main()