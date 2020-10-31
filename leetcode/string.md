# String

## Valid Anagram

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
