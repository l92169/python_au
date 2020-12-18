#Math

+ [Palindrome Number](#palindrome-number)

##Palindrome Number

https://leetcode.com/problems/palindrome-number/

``` python
def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    else:
        for i in range(0,len(str(x))//2):
            if (str(x))[i] != (str(x))[len(str(x))-i-1]:
                return False
        return True
```
