kg = float(input("Enter the weight in kilograms: "))

height = float(input("Enter the height in meters: "))

bmi = kg / (height ** 2)

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You are normal weight.")
else: print("You are Overweight.")
print("Your BMI is: ", bmi)