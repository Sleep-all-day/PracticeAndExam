class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return 0

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)

        return combinations

if __name__ =="__main__":
    s = Solution()
    digits = "23"
    ans = s.letterCombinations(digits)
    print(ans)
