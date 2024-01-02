''' Tarak Mehta Ka Ooltha Chasma'''

print("Hello gamer!!")
name=input("please! enter your name=>")
print("welcome!",name)
print("!!!!!Rules!!!!! \n 1.select any one character from TMKOC \n 2.answer the question in only Yes or No \n")
print("let's start.....guess any character ")
temp=input("are you ready???=>")
if(temp=="yes"):
    print("let's start!!")
    man=input("is your character is a men?=>")
    if(man=="yes"):
        sardar=input("is your character is sardarji?=>")
        if(sardar=="yes"):
            child=input("is your character is child?=>")
            if(child=="yes"):
                print("Your character is:GOGI")
            else:
                print("Your character is:ROSHAN SING SODHI")
        else:
            child=input("is your character is child?=>")
            if(child=="yes"):
               leader=input("is your character is a leader=>")
               if(leader=="yes"):
                   print("Your character is:TAPU")
               else:
                   fat=input("is your character is fat?=>")
                   if(fat=="yes"):
                       print("Your character is:GOLI")
                   else:
                       print("Your character is:PINKU")
            else:
                fat=input("is your character is fat?=>") 
                if(fat=="yes"):
                    print("Your character is:DR HANSHRAJ HAATHI")
                else:
                    glass=input("is your character wearing a glasses?=>")
                    if(glass=="yes"):
                        age=input("is your character is old in age?=>")
                        if(age=="yes"):
                            print("Your character is:CHAMPAKLAL GADA")
                        else:
                            married=input("is your character is married?=>")
                            if(married=="yes"):
                                black=input("is your character has black colorton?=>")
                                if(black=="yes"):
                                    print("Your character is:KRISHNAN AYER")
                                else:
                                    print("Your Character is:ATMARAM TUKARAM BHIDE")
                            else:
                                print("Your character is:POPATLAL PANDAY")
                    else:
                        gujarati=input("is your character love jalebi fafda?=>")
                        if(gujarati=="yes"):
                            print("Your character is:JETHALAL GADA")
                        else:
                            writer=input("is your character is writer?=>")
                            if(writer=="yes"):
                                print("Your character is:TARAK MEHTA")
                            else:
                                print("Your charcter is:ABDUL")
    else:
        child=input("is your character is child?=>")
        if(child=="yes"):
            print("Your character is:SONU")
        else:
            fat=input("is your character is fat?=>") 
            if(fat=="yes"):
                    print("Your character is:KOMAL HAATHI")
            else:
                businesswoman=input("is your character run a business?=>")
                if(businesswoman=="yes"):
                    print("Your character is:MADHVI BHIDE")
                else:
                    garba=input("is your character love doing garba?=>")
                    if(garba=="yes"):
                        print("Your character is:DAYABEN GADA")
                    else:
                        dait=input("is your character love dieat food?=>")
                        if(dait=="yes"):
                            print("Your character is:ANJALI MEHTA")
                        else:
                            exersice=input("is your character daily do exersice?=>")
                            if(exersice=="yes"):
                                print("Your character is:BABITAJI")
                            else:
                                print("Your character is:ROSHAN SODHI")

else:
    print("be ready",name)