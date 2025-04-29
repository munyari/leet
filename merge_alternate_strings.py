class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        shorter_len = min(len(word1), len(word2))
        for i in range(0, shorter_len):
            result.append(word1[i])
            result.append(word2[i])
        result.extend(word1[shorter_len:])
        result.extend(word2[shorter_len:])
        return "".join(result)

def test_merge_alternately():
    s = Solution()
    for word1, word2, expected in [
            ("foo", "bar", "fboaor"),
            ("", "bar", "bar"),
            ("bar", "", "bar"),
            ("foo", "barbaz", "fboaorbaz"),
    ]:
        assert s.mergeAlternately(word1, word2) == expected
    print("Tests passed")

test_merge_alternately()
