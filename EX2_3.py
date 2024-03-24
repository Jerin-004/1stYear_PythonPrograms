print("URK23CS1101 Jerin_Stalin")
condition = True
li = []
contact = ()
while condition:    
    print("")
    print("Choose your option: ")
    print("1.Add Contact: ")
    print("2.Search Contact: ")
    print("3.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        n = int(input("Enter how many contacts you want to enter: "))
        for i in range(n):
            name = input("Enter name: ")
            no = input("Enter number: ")
            contacts = (name,no)
            li.append(contacts)
            print(li)
            
    elif choice == 2:
        na = input("Enter person name to search: ")    
        for i in range(0,len(li)):
            if na == li[i][0]:
                print(li[i][0])
                print("Contact number: ",li[i][1])
    
    else:
        condition = False    

    
    