




print()
print("Welcome to Phone Book application.")
print()

book = [["johnny", "cake", "098765462839" ],["mary","wise","98038228493"],["andy","brown","0987625876"]]


while True :

    print("For adding a record, press the button \'c\'. For listing the records, press the button \'r\'.") 
    print("For updating the records, press the button \'u\'. For deleting a record, press the button \'d\'.")
    print("For exiting the program, press the button \'q\'. ")
    

    print()

    wish = input()

    if( wish == "q") :
        exit()
    elif(wish == "c") :
        name = input("please enter your contact's name ")
        last_name = input("please enter your contact's lastname ")
        number = input("please enter your contact's phone number ")
        new_record=[name, last_name, number]
        book.append(new_record)
        print()
        print("***",name, last_name, "is added successfully", "***", sep=" ")
        print()
    elif(wish == "r") :
        print()
        print("S.Nu:\tName \t  :\tPhone_Number :\t")
        print("----\t-----------\t---------------\t")
        for i in book :
            print(book.index(i)+1, i[0], i[1], i[2], sep="\t")
            print()
    elif(wish == "u"):
        name = input("please enter your contact's name ")
        last_name = input("please enter your contact's lastname ")
        is_found= False
        for i in book :
            if i[0] == name and i[1] == last_name :
                
                new_last_name,new_name,new_number="","",""

                print()
                name_change = input("Would you like to change your contact's name (Y/N) ")
                if(name_change.upper() == "Y"):
                    new_name = input("please enter your contact's new name ")
                
                last_name_change = input("Would you like to change your contact's lastname (Y/N) ")
                if(last_name_change.upper() == "Y"):
                    new_last_name = input("please enter your contact's new lastname ")
                
                number_change = input("Would you like to change your contact's number (Y/N) ")
                if(number_change.upper() == "Y"):
                    new_number = input("please enter your contact's new number ")

                if(new_name != ""):
                    i[0] = new_name
                    is_found = True
                if(new_last_name != ""):
                    i[1] = new_last_name 
                    is_found = True
                if(new_number != ""):
                    i[2] = new_number 
                    is_found = True
                
                if(is_found):
                    print("*** your contact is updated ***")
                    print()
                else :
                    print("*** your contact is not updated ***")
                    print()
                    is_found=True

        if(not is_found):
            print("*** the person you look for is not in the list ***")

    elif(wish == "d") :
        name = input("please enter your contact's name ")
        last_name = input("please enter your contact's lastname ")
        is_found= False
        for i in book :
            if i[0] == name and i[1] == last_name :
                is_found = True
                book.remove(i)
                print()
                print("*** your contact is deleted ***")
                print()

        if(not is_found) :
            print()
            print("*** the person you look for is not in the list ***")
            print()