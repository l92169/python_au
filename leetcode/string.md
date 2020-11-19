# Intervals

## Reverse Words in a String III

+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)

https://leetcode.com/problems/reverse-words-in-a-string-iii/

``` python
def reverseWords(self, s: str) -> str:
    d = s.split()
    new_str = ''
    for i in range(len(d)-1):
        d[i] = d[i][::-1]
        new_str = new_str + str(d[i]) + ' '
    d[len(d)-1] = d[len(d)-1][::-1]
    new_str = new_str + str(d[len(d)-1])
    return new_str
```