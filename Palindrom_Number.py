# Step 1: Quick rejection for impossible cases
        # Negative numbers can't be palindromes (would start with - when reversed)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (except 0) can't be palindromes
        if x < 0 or (x % 10 == 0 and x!= 0):
            return False

        reversed_num = 0
        original = x
        # Reverse until halfway through the number
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        # Handle odd vs even length palindromes
        return x == reversed_num or x == reversed_num // 10
