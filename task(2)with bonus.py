a = "Yes"
b = "Yes"
while a == b:
    year = int(input("enter your birthday year: "))
    remainder = year % 12
    if remainder == 0:
        zodiac = "MONKEY"
    elif remainder == 1:
        zodiac = "ROSTER"
    elif remainder == 2:
        zodiac = "dog"
    elif remainder == 3:
        zodiac = "pig"
    elif remainder == 4:
        zodiac = "Rat"
    elif remainder == 5:
        zodiac = "OX"
    elif remainder == 6:
        zodiac = "Tiger"
    elif remainder == 7:
        zodiac = "rabbit"
    elif remainder == 8:
        zodiac = "Dragon"
    elif remainder == 9:
        zodiac = "Snake"
    elif remainder == 10:
        zodiac = "horse"
    elif remainder == 11:
        zodiac = "sheep"
    print("Your Chinese Zodiac sign is:", zodiac)
    a = input("Do you want to try again?? (Yes/No): ")
    if a=="No":
         print("Program endded")
         break
      
