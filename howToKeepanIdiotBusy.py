#how to keep an idiot busy for hours
import pyinputplus as pyip


while True:
    yesOrNo = pyip.inputYesNo("Do you want to keep an idiot busy? ")
    if yesOrNo == "no":
        print("Ok, goodbye.")
        break