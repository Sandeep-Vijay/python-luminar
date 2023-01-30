fixed_amount=100000
withdraw=float(input("Enter the amount to withdraw"))

balance=fixed_amount-withdraw


if withdraw<=fixed_amount:
    print("Balance amount is", balance)
else:
    print('insufficient fund')


