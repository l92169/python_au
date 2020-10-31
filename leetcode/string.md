# String

## Valid Anagram

+ [Valid Anagram](#valid-anagram)
+ [Valid Anagram](#valid-anagram)
+ [Valid Anagram](#valid-anagram)

https://leetcode.com/problems/valid-anagram/

``` python
def isAnagram(self, s: str, t: str) -> bool:
    first = []
    second = []
    if len(s) != len(t):
        return False
    else:
        for i in range(len(s)):
            first.append(s[i])
            second.append(t[i])
        first.sort()
        second.sort()
        if first == second:
            return True
        return False
```

https://leetcode.com/problems/valid-anagram/

``` python
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```

https://leetcode.com/problems/valid-anagram/

``` python
def isAnagram(self, s: str, t: str) -> bool:
    return self.count_char_freq(s) == self.count_char_freq(t)  
def count_char_freq(self, s: str):
    freq = {}
    for keys in s:
        freq[keys] = freq.get(keys, 0) +1
    return freq
```

