#String

+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)

##Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

``` python
def reverseVowels(self, s: str) -> str:
    glas = []
    new_str = ''
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'o' or s[i] == 'u' or s[i] == 'i' or s[i] == 'A' or s[i] == 'E' or s[i] == 'O' or s[i] == 'U' or s[i] == 'I':
            glas.append(s[i])
    j = len(glas) - 1
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'o' or s[i] == 'u' or s[i] == 'i' or s[i] == 'A' or s[i] == 'E' or s[i] == 'O' or s[i] == 'U' or s[i] == 'I':
            new_str = new_str + glas[j]
            j -= 1
        else:
            new_str = new_str + s[i]
    return new_str
```
