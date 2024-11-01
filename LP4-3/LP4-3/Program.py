eggs = int(input("Enter number of eggs to be bought: "))
dozens = eggs // 12
remainder = eggs % 12

if dozens > 0 and dozens < 4:
  price = 0.50
if dozens >= 4 and dozens < 6:
  price = 0.45
if dozens >= 6 and dozens < 11:
  price = 0.40
if dozens >= 11:
  price = 0.35
print("The bill is equal to: $" + str(round(price + ((price / 12) * remainder), 2)))

input()