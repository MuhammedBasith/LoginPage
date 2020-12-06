
def login():

    with open('C:\\Users\\hp\\Desktop\\ \\data.txt', 'r') as test:
        data = []
        for lines in test:
            data.append(lines.strip('\n'))
        # print(data)

        valid = False
        while not valid:

            username = input("Username: ")
            password = input("Password: ")

            if username in data:
                index_user = data.index(username)

            if username and password in data:
                if password == data[index_user + 1]:

                    print('Logged in successfully ! ')
                    valid = True

                else:
                    print("Invalid !")
            else:
                print("Please check your user and pass !")


def new_account():

    with open('C:\\Users\\hp\\Desktop\\ \\data.txt', 'a') as user_data:

        valid = False
        while not valid:

            new_user = input("Please enter a new username: ")
            new_pass = input("Please enter a new password: ")
            confirm_pass = input("Confirm password: ")

            with open('C:\\Users\\hp\\Desktop\\ \\data.txt', 'r') as check:

                check_data = []
                for lines in check:
                    check_data.append(lines.strip('\n'))

                if new_user in check_data:
                    print("That username already exists. ")

                else:

                    if new_pass == confirm_pass:

                        if len(new_user) > 6 and len(new_pass) > 6:

                            if ' ' in new_pass:
                                new_user = new_user.strip('\n')
                                new_pass = new_pass.strip('\n')
                                print(new_user, file=user_data)
                                print(new_pass, file=user_data)
                                input("Press enter to continue.. ")
                                print("Account successfully created.")
                                valid = True

                            else:
                                print("Should contain a space in password.")

                        else:
                            print("Should contain greater than 6 characters. ")
                    else:
                        print("Passwords doesn't match !!")


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
