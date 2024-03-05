''': Create a command-line BMI calculator in Python. Prompt users for their
weight (in kilograms) and height (in meters). Calculate the BMI and classify it into categories
(e.g., underweight, normal, overweight) based on predefined ranges. Display the BMI result and
category to the user.
'''
from decimal import Decimal

weight = int(input("Please ENTER your weight(kg): "))
height =Decimal(input("Please ENTER your height(meters): ")) 

#1.75m x 1.75m = 3m2.
#70kg ÷ 3m2 = 23.


def Calc_BMI(weight, height):
    height = height * height
    bmi = weight / height

    if bmi < 18.5:
        category = "Underweight"
    if bmi >= 18.5 and bmi <=24.9:
        category = "Normal Weight"
    if bmi >= 25 and bmi <= 29.9:
        category = "Overweight"
    if bmi >= 30:
        category ="Obese"

    return bmi, category

a, b = Calc_BMI(weight, height)

print(f"Your BMI is: {round(a)}\n You are {b}")
