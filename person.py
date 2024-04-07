
class Person:
    def __init__(self, name, height, weight, BMI, category):
        self.name = name
        self.height = height
        self.weight = weight
        self.category = category
        self.BMI = BMI

    def __str__(self):
        return str(self.name, self.height, self.weight, self. category, self.BMI)

@staticmethod
def parseAndConvert(height_input):
    # Parsing the height into 2 inputs
    parts = height_input.split()
    feet = int(parts[0])
    inches = int(parts[1])
    
    # Converting the height into feet and inches
    total_inches = feet * 12 + inches
    total_cm = total_inches * 2.54
    Person.height = total_cm
    total_cm = round(total_cm, 2)

    return total_cm

# def test_parseAndConvert():
#     assert parseAndConvert("5 10") == 177.8

@staticmethod
def poundToKilograms(weight_input):
    kilos = weight_input / 2.2
    kilos = round(kilos, 2)
    Person.weight = kilos
    
    return kilos

# def test_poundToKilograms():
#     assert poundToKilograms(130) == 59.09

@staticmethod
def calcBMI (total_cm, kilos):
    # Converting from cm to m
    height_meters = total_cm / 100
    BMI = kilos / (height_meters ** 2)
    BMI = round(BMI, 2)
    Person.BMI = BMI
    return BMI

# def test_calcBMI():
#     assert calcBMI(177.9, 59.09) == 18.67

@staticmethod
def BMIcat (BMI):
    if BMI < 18.5:
        Person.category = "Underweight"
    
    elif 18.5 <= BMI <= 24.9:
        Person.category = "Normal Weight"

    elif 25 <= BMI <= 29.9:
        Person.category = "Overweight"

    else:
        Person.category = "Obese"

    return Person.category

#@pytest.mark.parametrize("test,category", [(18, "Underweight"), (20, "Normal Weight"), (27, "Overweight"), (30, "Obese")])

# def test_BMIcat(test, category):
#     assert BMIcat(test) == category