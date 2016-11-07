#Author : Rahul Gaikwad
#Date : 12/11/2015
#File : m.py
from sE import SE

search = SE()
flag = 'yes'

while(flag == 'yes'):
    print ("(Note: all keywords you type are case sensitive.) \nSelect One Choice From Below.\n----Menu----")
    print ("call_number")
    print ("title")
    print ("subject")
    print ("other")
    print ("quit")
    inputstr = input()

    if (inputstr == 'quit') or (inputstr == 'title') or (inputstr == 'call_number') or (inputstr =='subject') or (inputstr == 'other'):
        if inputstr.upper().strip() == "QUIT":
            break
        
        print("Please enter a search string: ")
        
        searchString = input()

        if inputstr.upper().strip() == "TITLE":
            result = []
            result = search.search_by_title(searchString)
            if result:
                for line in result:
                    line.display()
        elif (inputstr.upper().strip() == "CALL_NUMBER"):
            result = []
            result = search.search_by_call_number(searchString)
            if result:
                for line in result:
                    line.display()
        elif (inputstr.upper().strip() == "SUBJECT"):
            result = search.search_by_subject(searchString)
            if result:
                for line in result:
                    line.display()
        elif inputstr.upper().strip() == "OTHER":
            result = search.search_by_other(searchString)
            if result:
                for line in result:
                    line.display()
        print ("Do you want to continue? type 'yes' and press 'Enter' to continue. To exit just press 'Enter'")
        new_input= input()
        if new_input == 'yes':
            pass
        else :
            break
            flag = 'no'
    else:
        print ("\n You have entered wrong choice. Please enter your choice again \n")
    
