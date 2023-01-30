 #5 1 2 3 4 5      1+2+3+4+5

def sum_of_n(n):
     if n==0:              #n=0
         return n
     else:
         return n+sum_of_n(n-1)
              # 5+sum_of_n(4)
               # 4+sum_of_n(3)
                # 3+sum_of_n(2)
                 # 2+sum_of_n(1)
                  # 1+sum_of_n(0)
print(sum_of_n(5))