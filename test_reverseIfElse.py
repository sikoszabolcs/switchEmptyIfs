import reverseIfElse
import unittest

class TestReverseIfElse(unittest.TestCase):

	 def test_findMinimal(self):
		testString = "if(a < b){}else{ alma korte banan }"
	 	matches, ifs, elses = reverseIfElse.findMinimal(testString)
	 	self.assertEqual(ifs[0], "a < b")
	 	self.assertEqual(elses[0], " alma korte banan ")
	 	for m in matches:
	 		self.assertEqual(9, m.start())
	 		self.assertEqual(16, m.end())

	 def test_findMinimal_with_complex_if_expression(self):
		testString = "if(a \n< \nb){}else{ alma korte banan }"
	 	matches, ifs, elses = reverseIfElse.findMinimal(testString)
	 	self.assertEqual(ifs[0], "a \n< \nb")
	 	self.assertEqual(elses[0], " alma korte banan ")
	 	for m in matches:
	 		self.assertEqual(11, m.start())
	 		self.assertEqual(18, m.end())

	 def test_determineIndentationOfRevStartCommentFromPos(self):
	 	testString = "\n\t  if(a < b){}else{ alma korte banan }"
	 	result = reverseIfElse.determineIndentationOfRevStartCommentFromPos(14, testString)
	 	self.assertEqual('\n\t  ', result)

	 def test_noEnterBeforeIf(self):
		testString = "if(a < b){}else{ alma korte banan }"
	 	result = reverseIfElse.determineIndentationOfRevStartCommentFromPos(9, testString)
	 	self.assertEqual('', result)

	 def test_noIfBeforeElse(self):
	 	testString = "f(a < b){}else{ alma korte banan }"
	 	self.assertRaises(Exception, reverseIfElse.determineIndentationOfRevStartCommentFromPos, 0, testString)

	 def test_withFile(self):
	 	testString = "if(a>b){}else{if(alma){}else{int t =0;\nint c=1;}}"
		matches, ifs, elses = reverseIfElse.findMinimal(testString)
		self.assertEqual(2, len(ifs))
		self.assertEqual(2, len(elses))

	 def test_insertElseIntoIf(self):
		testString = "if(a>b){}else{test}"
		result = reverseIfElse.insertElseIntoIf(testString)
		self.assertEqual("if(a>b){test}", result)

	 def test_insertElseIntoIf_Variation(self):
	 	testString = "if(a>b){}else{\n\ttest();\n\tint i=0;\n}"
		result = reverseIfElse.insertElseIntoIf(testString)
		self.assertEqual("if(a>b){\n\ttest();\n\tint i=0;\n}", result)
	 
	 def test_insertElseIntoIf_with_embedded_If(self):
	 	testString = "if(a>b){}else{if(elephant>moon){}else{everythingFine();}}"
		result = reverseIfElse.insertElseIntoIf(testString)
		self.assertEqual("if(a>b){if(elephant>moon){everythingFine();}}", result)

	 def test_insertElseIntoIf_with_embedded_If_with_whitespaces(self):
	 	testString = "if(a>b) \n{\n    \n   \n}else{\n\tif(elephant>moon){\n }\nelse\n{\n\t\teverythingFine();\n\t\tbutThatsGoingToChange();}}"
		result = reverseIfElse.insertElseIntoIf(testString)
		self.assertEqual("if(a>b) \n{\n\tif(elephant>moon){\n \n\t\teverythingFine();\n\t\tbutThatsGoingToChange();}}", result)


if __name__ == '__main__':
	unittest.main()