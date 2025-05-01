# Valid palindrome ii

Link: https://leetcode.com/problems/valid-palindrome-ii/

# Assumptions
- string is all lowercase english letters
- strings are non-empty

# Examples
```python
"a" -> True
"ab" -> True
"aba" -> True
"raceecar" -> True
"racecar" -> True
"raccar" -> False
```

# Naive Approach
We can break this down recursively.
Base cases:
len = 0: valid palindrome
len = 1: valid palindrome
len = 2: valid 1-off palindrome
3 recursive cases. is valid palindrome if:
- you delete first character, and the remainer is a valid palindrome 
- you delete the last character, the remainder is a valid palindrome 
- you delete first and last character, the remainder is a valid 1-off palindrome

this can be modeled with a recursive solution

```python
    def perfectPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and perfectPalindrome(s[1:-1])

    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True
        return self.perfectPalindrome(s[1:]) or \
            self.perfectPalindrome(s[:-1]) or \
            (s[0] == s[-1] and self.validPalindrome(s[1:-1]))
```

This is O(n^3) runtime by the following reasoning.
Consider perfectPalindrome. It makes about n/2 recursive calls, and copies the string `s[1:-1]`, which is O(n), at each level.
So perfectPalindrome is O(n^2).

validPalindrome in the worst case also makes n/2 recursive calls. At each recursive call, it performs the quardratic palindrome check.
So overall validPalindrome is O(n^2)

# Improved Approach
We can use the recurrence relations we found above and make them iterative.
The first `if` condition in the loop maps to the `self.validPalindrome(s[1:-1])` call: consume end characters that are identical.
When we come to the first character where that fails, we try to see if [front+1,back] is a perfect palindrome. If it is, we return true.
If not, we take our last shot with [front,back-1].

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        front, back = 0, len(s)-1
        while front < back:
            if s[front] == s[back]:
                front += 1
                back -= 1
                continue
            front2 = front+1
            back2 = back
            while front2 < back2:
                if s[front2] != s[back2]:
                    break
                front2 += 1
                back2 -= 1
            if front2 >= back2:
                return True
            front2 = front
            back2 = back-1
            while front2 < back2:
                if s[front2] != s[back2]:
                    return False
                back2 -= 1
                front2 += 1

            if front2 >= back2:
                return True

        return True

```

Here's a slighlty more succinct version that reduces redundant code and cases:

```python
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
```

O(1) space
O(n) time
