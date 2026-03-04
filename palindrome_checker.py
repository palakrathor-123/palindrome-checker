def is_palindrome(s):
    # s[::-1] reverses the string
    return s == s[::-1]

print(is_palindrome("radar"))  
print(is_palindrome("hello"))