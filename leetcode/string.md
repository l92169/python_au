#String

##Reverse String

+ [Reverse String](#reverse-string)

https://leetcode.com/problems/reverse-string/

``` python
def reverseString(self, s: List[str]) -> None:
    for i in range(len(s) // 2):
        t = s[len(s)- 1 - i]
        s[len(s) - 1 - i] = s[i]
        s[i] = t
    return s
```