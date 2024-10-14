weight = int(input("Enter package weight in kilograms: "))
length = int(input("Enter package length in centimeters: "))
width  = int(input("Enter package width in centimeters: "))
height = int(input("Enter package height in centimeters: "))

dimensions = width * length * height

if weight > 27 and dimensions > 100000:
    print("Too heavy and too large.")
elif weight > 27 and dimensions < 100000:
    print("Too Heavy.")
elif weight < 27 and dimensions > 100000:
    print("Too large.")
else:
    print ("Good too go.")
    
input()

