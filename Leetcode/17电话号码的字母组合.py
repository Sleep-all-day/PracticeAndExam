class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return 0

        phoneMap = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "xyz"
        }



