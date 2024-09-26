class Solution:
    def compress(self, chars: List[str]) -> int:
        f, s, n = 0, 0, len(chars)
        while f < n:
            j = s + 1
            while j < n and chars[j] == chars[f]:
                j += 1
            chars[s] = chars[f]
            s += 1
            if j - f > 1:
                cnt = str(j - f)
                for c in cnt:
                    chars[s] = c
                    s += 1
            f = j
        return s