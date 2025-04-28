from __future__ import annotations
from typing import List, Optional
from dataclasses import dataclass


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opens = []
        closes = []
        for i, c in enumerate(s):
            if c == '(':
                opens.append(i)
            if c == ')':
                if opens:
                    opens.pop()
                else:
                    closes.append(i)

        indexes_to_remove = set(opens+closes)
        return ''.join(
            c for i, c in enumerate(s) if i not in indexes_to_remove
        )

def test_min_remove():
    s = Solution()
    for case, expected in [
            ("()", "()"),
            ("(abc)", "(abc)"),
            ("(abc", "abc"),
            ("ab)c", "abc"),
            ("((a(b)c", "a(b)c"),
    ]:
        actual = s.minRemoveToMakeValid(case)
        assert actual == expected, f"{case=} {expected=} {actual=}"
    print("Tests passed")

test_min_remove()
