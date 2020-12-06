import sqlite3
import sys

db = sqlite3.connect("C:\\Users\\hp\\Desktop\\ \\data.db")
db.execute('create table if not exists user_info (username text, password text) ')


def login():
    valid = False
    while not valid:

        username = input("Username: ")
        password = input("Password: ")

        cursor = db.execute("select * from user_info where username = ?", (username,))
        retrieved = cursor.fetchone()
        # print(retrieved)

        if retrieved:
            if retrieved[1] == password:

                print('Logged in successfully ! ')
                valid = True

            else:
                print("Please check your password! ")

        else:
            print("Invalid username! ")


def new_account():

    valid = False
    while not valid:

        new_user = input("Please enter a new username: ")

        read = db.execute('select * from user_info')
        values_read = read.fetchall()

        whole = [tup for val in values_read for tup in val]

        if new_user in whole:
            print("Sorry that username is already taken ! ")

        else:
            new_pass = input("Please enter a new password: ")
            confirm_pass = input("Confirm password: ")

            if new_pass == confirm_pass:

                if len(new_user) > 6 and len(new_pass) > 6:

                    if ' ' in new_pass:

                        cursor = db.execute("insert into user_info values(?, ?)", (new_user, new_pass))
                        cursor.connection.commit()

                        input("Press enter to continue.. ")
                        print("Account successfully created.")
                        valid = True

                    else:
                        print("Should contain a space in password.")

                else:
                    print("Should contain greater than 6 characters. ")
            else:
                print("Passwords do not match !!")


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
            sys.exit(1)

        else:
            print("That's not a valid input !")


# ---------------------------------------------- Main Body -----------------------------------------------------------


display()
