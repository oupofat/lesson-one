'''Tip Calculator
The user just finished a meal at a restaurant. Ask the user for:

the amount of the bill
what percentage they want to add as a tip
and then tell them

the tip amount, and
the total amount.'''

bill = float(input("What was the bill?"))
percentage = float(input("What percentage of tip do you want?"))
tip = bill * percentage /100
total = tip + bill
print("Total for this is",total,".")