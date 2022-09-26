height=float(input("Enter the height in cm:"))
weight=float(input("Enter the weight in kg:"))
BMI=weight/(height/100)**2
print("your body mass index is",BMI)
if BMI <= 18.5:
    print("you are under weight.")
elif BMI <= 24.9:
    print("Awsome ! you are Healthy good to go.")
elif BMI <= 29.9:
    print("oops you are unhealthy.")
else:
    print("you are obese^^^^^^")