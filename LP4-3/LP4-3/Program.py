Eggs = int(input("Enter # of Eggs to print: "))
dozen = round
price  = 0.0
cost   = 0.0


if dozen > 0 and dozen < 4:
    price = 0.50
elif dozen > 4 and dozen < 6:
    price = 0.45
elif dozen > 6 and dozen < 11:
    price = 0.40
elif dozen > 11:
    price = 0.35
else:
    print("Invalid # of Eggs")
    
cost = Eggs * price
print("Price per Dozen is $" + str(price))
print("Total cost is $" + str(round(cost,2)))
input() # Press 'Enter' to close; only needed for SharpDevelop
