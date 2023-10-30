# LeetCode: 13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = { "I": 1, "V": 5, "X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        intN, preN = 0, roman[s[0]]
        for x in s[1:]:
            if preN < roman[x]: intN -= preN
            else: intN += preN
            preN = roman[x]
        intN += preN
        return intN

if __name__ == "__main__":
    print(Solution().romanToInt("MCMXCIV"))