a = "yes"
b = "yes"
while b == a:
    weight = float(input())
    height = float(input())
    bmi = weight / (height * height)
    if bmi < 18.5:
        catagory = "underweight"
    elif 18.5 <= bmi <= 24.9:
        catagory = "normal weight"
    elif 25.0 <= bmi <= 29.9:
        catagory = "overweight"
    else:
        catagory = "obezz"
    print("BMI =", bmi)
    print("catagory:", catagory)
    a = input("Do you want ti try againn?? (yes/no): ")
    if a!=b:
        print("program is endded")
        break
