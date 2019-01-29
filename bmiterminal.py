#! /usr/local/bin/python3

def bmi():
    #! Function Level Variables
    name = input("Your name: ")
    gender = input("Your Gender:[m/f] ")
    height = float(input("Enter your height in meters[1.70]: "))
    weight = float(input("Enter your weight in kgs[80.2]: "))
    height_new = height * height
    bmi = float(weight / height_new)

    #! Gender Definition
    if gender == 'm':
        if bmi > 0 and bmi < 60:
            print("Hello, ", name, " Your BMI is: ", bmi)
            if bmi > 0 and bmi < 18.5:
                print("You are underweight")
            elif bmi >= 18.5 and bmi <= 24.9:
                print("You are normalweight")
            elif bmi >= 25 and bmi <= 29.9:
                print("You are overweight")
            elif bmi >= 30 and bmi <= 34.9:
                print("You are obese")
            elif bmi >= 35 and bmi <= 39.9:
                print("You have obese Grade II")
            elif bmi >= 40:
                print("You have obese Grade III")
        else:
            print("Invalid entries")
    elif gender == 'f':
        if bmi > 0 and bmi < 60:
            print("Hello, ", name, " Your BMI is: ", bmi)
            if bmi > 0 and bmi < 19:
                print("You are underweight")
            elif bmi >= 19 and bmi <= 24:
                print("You are normalweight")
            elif bmi >= 25 and bmi <= 30:
                print("You are overweight")
            elif bmi >= 31 and bmi <= 40:
                print("You are obese")
            elif bmi >= 41:
                print("You are strongly obese")
        else:
            print("Invalid entry")
    else:
        print("Invalid entries")

bmi()
