class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        b = x[::-1]
        if x == b:
            return True
        else:
            return False

x = Solution()
x.isPalindrome(input())