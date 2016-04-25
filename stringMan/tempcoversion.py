# temp conversion

def menu():
    print ("\1. celsius to fahrenite")
    print ("\2. fahrenite to celsius")
    print ("\3. Exit")
    user_input = int(input("enter a choice:"))
    return user_input

def tocelcies(fe):
    return int((fe-32)/1.8)

def tofahrenite(c):
    return int(c * 1.8 + 32)

def main():
    choice = menu()
    while choice != 3:
        if choice == 1:
            c = input("enter degree celsius:")
            print (str(tofahrenite(c)))
        elif choice ==2:
            f = input("enter degree fahrenite:")
            print (str(tocelcies(f)))
          
        else:
            print ("invalid menu")
        choice = menu()


main()