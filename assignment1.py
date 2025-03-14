marksheet=[]
print("\nMarksheet generator.\nProvide data of students and generate marksheet.\n")

i=0

action1 = ""
while True:
    if action1 == "no" or action1 == "No":
        break
    action:str = str(input("\n\nDo you want to add data of student for marksheet (yes or no) : "))
    if action == "yes" or action == "Yes":
        while True:
            nameOfStudent:str = str(input("\nType name of student : "))
        
            fatherName:str = str(input("Type father name of student : "))
        
            rollNo:int = int(input("Type roll number of student : "))
        
            print("\nNow Enter obtained marks of subjects,\nMarks should be less than 100 :-\n")
            sub1o:float = float(input("Type obtained marks of Math : "))
        
            sub2o:float = float(input("Type obtained marks of Physics : "))
        
            sub3o:float = float(input("Type obtained marks of Chemistry : "))
        
            sub4o:float = float(input("Type obtained marks of Urdu : "))
       
            sub5o:float = float(input("Type obtained marks of English : "))
        
            sub6o:float = float(input("Type obtained marks of Islamiat : "))
        
            total:float = 600
        
            obtained:float = sub1o+sub2o+sub3o+sub4o+sub5o+sub6o
        
            percentage = obtained/total*100
        
            grade = "?"
            if percentage<=49:
                grade = "F"
            elif percentage<=59:
                grade = "C"
            elif percentage<=69:
                grade = "B"
            elif percentage<=79:
                grade = "A"
            elif percentage>=80:
                grade = "A+"


            if sub1o>100 or sub2o>100 or sub3o>100 or sub4o>100 or sub5o>100 or sub6o>100:
                print("\n\nPlease enter marks less than 101")
                continue

            i+=1

            marksheet.append(f"Student {i} = "+"Name : " + nameOfStudent+", Father name : " + fatherName+", Roll number : " + str(rollNo)+", Marks of Math : " + str(sub1o)+", Marks of Physics : " + str(sub2o)+", Marks of Chemistry : " + str(sub3o)+", Marks of Urdu : " + str(sub4o)+", Marks of English : " + str(sub5o)+", Marks of Islamiat : " + str(sub6o)+", Total marks : " + str(total)+", Obtained marks : " + str(obtained)+", Percentage : " + str(percentage) + " % "+", Grade : " + grade + "      |--x--|      ")


            print("\n\t__________________________________\n\n")
            print("\t\t Marksheet\n\n")
            print(f"\t Name        : {nameOfStudent}")
            print(f"\t Father name : {fatherName}")
            print(f"\t Roll number : {rollNo}")
            print(f"\t Percentage  : {percentage} %")
            print(f"\t Grade       : {grade}")
            print("\n\t__________________________________\n\n")
            print("\t Math        :\t%.1f / 100"%(sub1o))
            print("\t Physics     :\t%.1f / 100"%(sub2o))
            print("\t Chemistry   :\t%.1f / 100"%(sub3o))
            print("\t Urdu        :\t%.1f / 100"%(sub4o))
            print("\t English     :\t%.1f / 100"%(sub5o))
            print("\t Islamiat    :\t%.1f / 100"%(sub6o))
            print("\n\t__________________________________\n\n")
            print("\t Total  = \t%.1f / %.1f"%(obtained,total))

            print(f"Data of {nameOfStudent} entered successfully.")
            action1:str = str(input("\n\nDo you want to add more data of student for marksheet (yes or no) : "))
            if action1 == "yes" or action1 == "Yes":
                continue
            elif action1 == "no" or action1 == "No":
                break

            else:
                print(f"\nPlease type \" yes \" or \" no \", you typed \" {action} \" and it will be considered \" no \"\n")
                break
            

    elif action == "no" or action == "No":
        break

    else:
        print(f"\nPlease type \" yes \" or \" no \", you typed \" {action} \"\n")
        continue
    
print("\n\nData you provided :-\n")
print(marksheet)    
