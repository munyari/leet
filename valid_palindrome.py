class Solution:
    def checkPalindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        front, back = 0, len(s)-1
        while front < back:
            if s[front] != s[back]:
                return self.checkPalindrome(s, front+1, back) or self.checkPalindrome(s, front, back-1)
            
            front += 1
            back -= 1

        return True

def test_valid_palindrome():
    s = Solution()
    for input_string, expected in [
            ("", True),
            ("a", True),
            ("ab", True),
            ("aa", True),
            ("racecar", True),
            ("racar", True),
            ("scientist", False),
            ("racer", False),
            ("cbbcc", True),
    ]:
        assert s.validPalindrome(input_string) == expected
    print("Tests passed")

test_valid_palindrome()
