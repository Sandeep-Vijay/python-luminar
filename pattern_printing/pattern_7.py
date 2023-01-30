#    *
#   * *
#  * * *
# * * * *
n=3
for i in range(4):
    for space in range(n):
        print('',end=' ')
    n=n-1
    for space in range(i+1):
        print('*',end=' ')
    print()


# n=5
# for row in range(5):
#     for space in range(n):
#         print(end=' ')
#     n=n-1
#     for col in range(row):
#         print('*',end=' ')
#     print()