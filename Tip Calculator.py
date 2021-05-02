meal = float(input("Enter your meal amount: "))
tip = int(input("Enter your tip percentage: "))
tax = .10

#calcs

tip_amt = meal * tip/100
tax_amt = meal * tax
total = meal + tip_amt + tax_amt

print(f"\nYour meal was ${meal:.2f} and your tip was ${tip_amt:.2f}.")
print(f"Your total with tax was ${total:.2f}.\n")