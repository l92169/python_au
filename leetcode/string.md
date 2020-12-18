# Intervals

+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)

## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/

``` python
def reverseWords(self, s: str) -> str:
    d = s.split()
    new_str = ''
    if s == '':
        return ''
    else:
        for i in range(len(d)-1):
            d[i] = d[i][::-1]
            new_str = new_str + str(d[i]) + ' '
        d[len(d)-1] = d[len(d)-1][::-1]
        new_str = new_str + str(d[len(d)-1])
        return new_str
```
