#fizzbuzz

#divisible by 3 print fizz
#divisible by 5 print buzz
#divisible by 15 print fizzbuzz

# 30 fizzbuzz
# 15 fizzbuzz
# 10 buzz
# 9 fizz

#code
num=15
if num%15==0:
    print("fizzbuzz")
elif num%5==0:
    print('buzz')
elif num%3==0:
    print("fizz")
else:
    print('in else')
