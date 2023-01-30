# #+919897654567
#
# import re
# x='[+][9][1][0-9]{10}'
# s=input('enter the number')
# matcher=re.fullmatch(x,s)
# if matcher is not None:
#     print('valid')
# else:
#     print('Invalid')
# ------------------------
#
# KL17R4046
#
# import re
# x='KL[\d]{2}[A-Z][\d]{4}'
# s=input('enter the number')
# matcher=re.fullmatch(x,s)
# if matcher is not None:
#     print('valid')
# else:
#     print('Invalid')
# -----------------------------
#
# string starts with a and end up with b
# ab  akjdfhkflkdjdkfb   aaaaaaabbbb
#
# import re
# x='^a[\w\W]*b$'
# s=input('enter the string')
# matcher=re.fullmatch(x,s)
# if matcher is not None:
#     print('valid')
# else:
#     print('invalid')
#
#
# string
# numbers special
# exact count 5
#
# 12345 3123^ #()@#d *&^09
#
#
# import re
# x='[\d\w\W]{5}'
# s=input('enter the string')
# matcher=re.fullmatch(x,s)
# if matcher is not None:
#     print('VALID')
# else:
#     print('INVALID')
#
# string with uppercase and lowercase
# minimum count 3 maximum  4
#
#
# import re
# x='[a-zA-Z]{3,6}'
# s=input('enter the string')
# matcher=re.fullmatch(x,s)
# if matcher is not None:
#     print('VALID')
# else:
#     print('INVALID')
#
# string start and end with zero
# minimum count 5 and maximum 10
# 0123453 000000
# import re
# x='^0[\w\W]{3,8}0$'
# s=input('enter the string')
# matcher=re.fullmatch(x,s)
# if matcher is not None:
#     print('VALID')
# else:
#     print('INVALID')
#
# string with special character
# last element a number or small letter
# exact count 4  eg $%#5 ()@y
#
# import re
# x='[\W]{3}[\da-z]$'
# s=input('enter the string')
# matcher=re.fullmatch(x,s)
# if matcher is not None:
#     print('VALID')
# else:
#     print('INVALID')