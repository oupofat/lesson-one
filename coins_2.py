'''Coin Counter
The user has an assortment of coins: quarters, dimes, nickels, and pennies.

Ask the user how many of each type of coin they have. Tell them the total monetary amount of their coins.'''

q=int(input("How many quarters do you have?"))
d=int(input("How many dimes do you have?"))
n=int(input("How many nickels do you have?"))
p=int(input("How many pennies do you have?"))
quart = quart*.25
dime = dime*.10
nick = nick*.05 
penn = penn*.01

total = quart + dime + nick+ penn
print("The total amount of money you have is",total,"!")


#you can't have q, d, n, p as a variable name
print ("Enter the number of quarters, dimes, nickels, and pennies you have")
print ("Spearated by spaces")

q,d,n,p = input().split(" ")
q = q*.25
d = d*.10
n = n*.05
p = p*.01
total = q + d + n+ p
print("The total amount of money you have is",total,"!")

