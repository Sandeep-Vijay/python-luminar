# keywords
#1.break
#2.continue

#1.break
## it stops current iteration and the upcoming iterations

for i in range(5):
    if i==2:
        break
    print(i)

# for                        if break doesn't work else will work
#     break                  if break works else will not work
# else                       if we use break in a for loop we can use else