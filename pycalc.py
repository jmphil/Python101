# Tip Calculator



meal = float(input("Enter meal amount:"))
tip = str(input("How was your service?"))

if tip == ('good'):
    print(f"\nTip amount: {meal * .20:.2f}")
elif tip == ("fair"):
    print(f"\nTip amount: {meal * .15:.2f}")
else :
    print (f"\nTip amount: {meal * .10:.2f}")

# tip_amount = int(meal * tip/100)
# total = meal + tip


# print(f"\nTip amount: {tip * meal:.2f}")
# print(f"\nTotal amount: {meal + tip * meal:.2f}")