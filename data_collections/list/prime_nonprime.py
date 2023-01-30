l=[1,2,3,4,5,6,7,8,9,10]
# prime
# non prime

lp=[]
lnp=[]
for i in l:
        for j in range(2,i):
            if i%j==0:
                lnp.append(i,)
                break

        else:
            lp.append(i)


lp.append('prime numbers')
lnp.append('non prime numbers')
print(lp)

print(lnp)










# # order sort #assending