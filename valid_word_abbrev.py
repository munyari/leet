class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_p = abbr_p = 0
        while word_p < len(word) and abbr_p < len(abbr):
            if word[word_p] == abbr[abbr_p]:
                word_p += 1
                abbr_p += 1
            elif abbr[abbr_p] == "0":
                return False
            elif abbr[abbr_p].isdigit():
                i = abbr_p
                while i < len(abbr) and abbr[i].isdigit():
                    i += 1
                word_p += int(abbr[abbr_p:i])
                abbr_p = i
            else:
                return False
        return word_p == len(word) and abbr_p == len(abbr)

def test_valid_word_abbreviation():
    s = Solution()
    for word, abbr, expected in [
        ("foo", "foo", True),
        ("foo", "f2", True),
        ("foo", "3", True),
        ("", "0", False),
        ("bar", "1a1", True),
        ("foobar", "foo4", False),
        ("leetcode", "leetc1de", True),
        ("leetcode", "leetc1de1", False)
    ]:
        assert s.validWordAbbreviation(word, abbr) == expected, f"{word=} {abbr=} {expected=}"
    print("tests passed")

test_valid_word_abbreviation()
