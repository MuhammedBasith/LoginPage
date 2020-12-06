import shelve


def login():

    user_data = shelve.open('data_dict')

    valid = False
    while not valid:

        username = input("Username: ")
        password = input("Password: ")

        try:
            if user_data[username] == password:
                print('Logged in successfully ! ')
                valid = True
            else:
                print("Please check your password!")

        except KeyError:
            print('Recheck your username! ')


def new_account():

    user_data = shelve.open('data_dict')

    valid = False
    while not valid:

        new_user = input("Please enter a new username: ")
        new_pass = input("Please enter a new password: ")
        confirm_pass = input("Confirm password: ")

        if new_pass == confirm_pass:

            if len(new_user) > 6 and len(new_pass) > 6:

                if ' ' in new_pass:

                    user_data[new_user] = new_pass

                    input("Press enter to continue.. ")
                    print("Account successfully created.")
                    valid = True

                else:
                    print("Should contain a space in password.")

            else:
                print("Should contain greater than 6 characters. ")
        else:
            print("Passwords doesn't match !!")

        user_data.close()


def display():

    valid = False
    while not valid:

        print('Choose one; ')
        prompt = input('1. Create an account. \n2. Already have an account ? Login. \n3. Quit \n:')

        if prompt == '1':
            new_account()
            valid = True

        elif prompt == '2':
            login()
            valid = True

        elif prompt == '3':
            quit()

        else:
            print("That's not a valid input !")


# ---------------------------------------------- Main Body -----------------------------------------------------------


display()
