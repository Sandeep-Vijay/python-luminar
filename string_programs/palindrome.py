#palidrome

#malayalam word is palindrome ##same word when reversing

s=input('enter the word to check palindrome')

if s==s[::-1]:
    print('palindrome')
else:
    print('not palidrome')