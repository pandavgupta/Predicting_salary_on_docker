from os import system
import joblib
model=joblib.load("/root/salary.pk1")
while True:
    system("clear")
    print("\n------------------------------------------------------------------------------")
    system("tput setaf 1")
    print("Here you can find your approximate salary according to your Year of Experience")
    system("tput setaf 7")
    print("------------------------------------------------------------------------------")
    yearOfExp=float(input("\n Enter how much year of experiance you have : "))
    result=model.predict([[yearOfExp]])
    print("\n Your Expected Salary is",round(result[0][0]),"INR.")
    cont=input("\n Do you want cont.(yes/no) :")
    if cont== "yes" or cont =="y" or cont=="Y" or cont=="YES":
        pass
    else:
        print(" Okay byyyy...")
        system("sleep 1")
        exit()

