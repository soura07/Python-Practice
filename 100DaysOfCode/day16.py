john = int(input("Enter you case no: \n"))

match john:
    case 0:
        print("Hey John you are in Case 0")
    case 1:
        print("Hey John you are in Case 1")
    case 2:
        print("Hey John you are in Case 2")
    case 3:
        print("Hey John you are in Case 3")
    
    case _:
        print("Which you entered this is none of this case...")    