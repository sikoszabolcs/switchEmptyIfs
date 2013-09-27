import reverseIfElse
import unittest

class TestReverseIfElse(unittest.TestCase):

	def test_oneIf_ShouldResult_InOneResult(self):
		testString = "if(a < b){}"
		result = reverseIfElse.findNestedString(testString)
		self.assertEqual(len(result), 1)

	def test_oneIf_ShouldResult_InExpressionBetweenBrackets(self):
		testString = "if(a < b){}"
		result = reverseIfElse.findNestedString(testString)
		self.assertEqual(result[0], "a < b")

	def test_oneIfWithNestedBrackets_ShouldResult_InExpressionBetweenFirstPairOfBrackets(self):
		testString = "if( (a == b) < (b + foo)){}"
		result = reverseIfElse.findNestedString(testString)
		self.assertEqual(result[0], " (a == b) < (b + foo)")

	def test_oneInvalidIf_ShoudlResult_InError(self):
	 	testString = "if(a < b{}"
	 	self.assertRaises(NameError, reverseIfElse.findNestedString, testString)

	def test_twoIf_ShouldResult_InTwoResults(self):
	 	testString = "if(a < b) {} if(c == d) {}"
	 	result = reverseIfElse.findNestedString(testString)
	 	self.assertEqual(len(result), 2)

	def test_missingCurlyBraces_ShouldResult_InNoMatch(self):
		testString = "if(a < b)"
	 	result = reverseIfElse.findNestedString(testString)
	 	self.assertEqual(len(result), 0)

	def test_anythingOtherThanWhitespaseWithinCurlyBraces_ShouldResult_InNoMatch(self):
		testString = "if(a < b){ something }"
	 	result = reverseIfElse.findNestedString(testString)
	 	self.assertEqual(len(result), 0)

if __name__ == '__main__':
	unittest.main()