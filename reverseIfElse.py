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
	#if\s*\(+.*\)+\s*\{\s*\}\s*else\s*\{((?:[^{}]+?|\{(?1)\}))+?\}
	#<[^<>]*(((?<Open><)[^<>]*)+((?<Close-Open>>)[^<>]*)+)*(?(Open)(?!))> 
	#\{(?:[^|}]+)?([^}]+)\}
	#\[\[(?:[^\]|]*\|)?([^\]|]*)\]\]
	#if\s*\(+.*\)+\s*\{\s*\}\s*else\s*\{((?:[^{}]++|\{(?1)\}))++\}
	#\{((?:[^{}]++|\{(?1)\}))++\}
	#Clear form: \{((?:[^{}]++|\{(?1)\}))++\}
	#return re.finditer(r"if\s*\(+.*\)+\s*\{{1}\s*\}{1}\s*else\s*\{((?:[^{}]++|\{(?1)\}))++\}", searchStr)
	#\{([^{}]+|\{(\1)\})+
	#if\s*\(+\s*.*\s*\)+\s*\{\s*\}\s*else\s*\{([^{}]+|\{.*\})+

	#\{$(?:\n^.+$)*\n^\}$
	#prog = re.compile('if\s*\(+.*\)+\s*\{{1}\s*\}{1}\s*else\s*\{$(?:\n^.+$)*\n^\}$', re.MULTILINE)
	# This works: prog = re.compile('\{$.*?^\}$', re.DOTALL | re.MULTILINE)
	#prog = re.compile('\{$.*?^\}$', re.DOTALL | re.MULTILINE)
	#$\s*\{\s*\}
	prog = re.compile(r'\{$.*?^\}$', re.DOTALL | re.MULTILINE)
	
	return prog.finditer(searchStr)


#def getElseBodyPart():

#def getIfExpression():

#def negateExpression():

#def switchIfBodyWithElseBody():

#def readAllFilesFromFolder(folder):

def main():
	fileName = "d:\Views\evoSiSz0_ESF_CoreDev_002.001_AT_pre\ESF_CORE\dev\logic\src\BaseSI.cpp"
	fileContents = getFileContents(fileName)
	matches = findIfWithEmptyBodyInString(fileContents)
	count = 0
	for m in matches:
		print '--------------------------------------------\n'
		print m.group()
		print count
		count += 1
		print '++++++++++++++++++++++++++++++++++++++++++++\n'

		#print 'IF Expression: %s \n +++++++ \n ELSE Contents: \n %s \n --------' % (m.group(1), m.group(2))
		#print 'start: %d end: %d' % (m.start(1), m.end(1))

if __name__ == "__main__":
	main()