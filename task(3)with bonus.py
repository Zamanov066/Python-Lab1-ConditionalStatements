a = "Yes"
b = "Yes"
while a == b:
    day = 0
    ans1 = int(input("Is your birthday in Set1? (1 for Yes, 0 for No): "))
    if ans1 == 1:
        day += 1
    ans2 = int(input("Is your birthday in Set2? (1 for Yes, 0 for No): "))
    if ans2 == 1:
        day += 2
    ans3 = int(input("Is your birthday in Set3? (1 for Yes, 0 for No): "))
    if ans3 == 1:
        day += 4
    ans4 = int(input("Is your birthday in Set4? (1 for Yes, 0 for No): "))
    if ans4 == 1:
        day += 8
    ans5 = int(input("Is your birthday in Set5? (1 for Yes, 0 for No): "))
    if ans5 == 1:
        day += 16
    print("Your birthday is:", day)
    a = input("Do you want to try again?? (Yes/No): ")s
