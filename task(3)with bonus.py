a = "Yes"
b = "Yes"

while a == b:
    day = 0

    # Set 1
    print("\nSet 1:")
    print(" 1  3  5  7")
    print(" 9 11 13 15")
    print("17 19 21 23")
    print("25 27 29 31")
    ans1 = int(input("Is your birthday in Set1? (1 for Yes, 0 for No): "))
    if ans1 == 1:
        day += 1

    # Set 2
    print("\nSet 2:")
    print(" 2  3  6  7")
    print("10 11 14 15")
    print("18 19 22 23")
    print("26 27 30 31")
    ans2 = int(input("Is your birthday in Set2? (1 for Yes, 0 for No): "))
    if ans2 == 1:
        day += 2

    # Set 3
    print("\nSet 3:")
    print(" 4  5  6  7")
    print("12 13 14 15")
    print("20 21 22 23")
    print("28 29 30 31")
    ans3 = int(input("Is your birthday in Set3? (1 for Yes, 0 for No): "))
    if ans3 == 1:
        day += 4

    # Set 4
    print("\nSet 4:")
    print(" 8  9 10 11")
    print("12 13 14 15")
    print("24 25 26 27")
    print("28 29 30 31")
    ans4 = int(input("Is your birthday in Set4? (1 for Yes, 0 for No): "))
    if ans4 == 1:
        day += 8

    # Set 5
    print("\nSet 5:")
    print("16 17 18 19")
    print("20 21 22 23")
    print("24 25 26 27")
    print("28 29 30 31")
    ans5 = int(input("Is your birthday in Set5? (1 for Yes, 0 for No): "))
    if ans5 == 1:
        day += 16

    print("\nYour birthday is:", day)
    a = input("\nDo you want to try again?? (Yes/No): ")
