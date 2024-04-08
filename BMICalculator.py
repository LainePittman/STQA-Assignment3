# BMI Calculator slp519
import person
from person import Person


# Takes in a name
name = input("What name would you like to add: ")
# Applies height to person
Person.name = name
# Takes in a height
height_input = input("Enter your height in ft. and inches w/ a space inbetween: ")
# Converts height to cm
centimeters = person.parseAndConvert(height_input)
# Takes in weight in lbs
weight_input = int(input("Enter in your weight in pounds: "))
# Converts weight to kg
kilos = person.poundToKilograms(weight_input)
# Applies weight to person
person.weight = kilos
# Performs BMI calculation
BMI = person.calcBMI(centimeters, kilos)
# Applies a BMI category to person
category = person.BMIcat(BMI)

# This takes all of the results and prints them
print("Name: ", Person.name)
print("Height (cm): ", Person.height)
print("Weight (kg): ", Person.weight)
print("BMI:", Person.BMI)
print("Category: ", Person.category)
