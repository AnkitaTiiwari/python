#calculating BMI
def calculateBMI(h,w):
    BMI = round(w/(h ** 2),2)
    return BMI


weight = float(input("Enter your weight in kg : "))
height = float(input("Enter you height in meter : "))

bmi = calculateBMI(weight,height)

print(f"Your BMI is {bmi}")