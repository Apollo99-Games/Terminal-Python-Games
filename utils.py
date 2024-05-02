def get_input(max):
    valid_input = False
    while valid_input == False:
        try:
            user_input = int(input("Please enter your choice: "))
            if user_input <= max and user_input >= 1:
                return user_input
            else:
                print("Invaild Input")
        except:
            print("Invaild Input")
