print("Scolarship eligibility criteria")
name=input("Enter your name:")
roll_number=int(input("Enter your roll number:"))
DSA=int(input("Enter your DSA marks out of 100:"))
COAL=int(input("Enter your COAL marks out of 100:"))
DE=int(input("Enter your differential equation marks out of 100:"))
TBW=int(input("Enter your TBW marks  out of 100:"))
DS=int(input("Enter your discrete structure marks out of 100:"))
attendence=int(input("Enter your attendence marks out of 10:"))
total=500
obtained=DSA+COAL+DE+TBW+DS
percentage=obtained/total*100
if percentage>=85 and percentage<=100 and attendence>=8 and attendence<=10:
    print(f"dear student,your tatal marks are {obtained} \nyour percentage is {percentage} \nyou got A+ grade and you are eligible for 50%scholarship:")
elif percentage>=80 and percentage<=84 and attendence>=6 and attendence<=7:
    print(f"dear student,your tatal marks are {obtained} \nyour percentage is {percentage} \nyou got A grade and you are eligible for 50%scholarship:")
elif percentage>=75 and percentage<=80 and attendence>=5 and attendence<=6:
    print(f"dear student,your tatal marks are {obtained} \nyour percentage is {percentage} \nyou got B+ grade and you are eligible for 50%scholarship:")
elif percentage>=70 and percentage<=75 and attendence>=5 and attendence<=5:
    print(f"dear student,your tatal marks are {obtained} \nyour percentage is {percentage} \nyou got B grade and you are eligible for 50%scholarship:")
else:
    print(f"Dear student Your percentage and attendence are too low and you are not eligible for scholarship:")