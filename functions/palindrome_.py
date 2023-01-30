def palindrome(s):
    if s==s[::-1]:
        return 'palindrome'
    else:
        return'not palidrome'

print(palindrome('malayalam'))
print(palindrome('english'))
