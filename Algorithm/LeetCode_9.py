# LeetCode : 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
class BetterSolution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_num = 0

        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return x == reversed_num or x == reversed_num // 10

if __name__ == "__main__":
    print(Solution().isPalindrome(-121))
    print(BetterSolution().isPalindrome(-121))