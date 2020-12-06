import pickle

users = {}


def display():

    while True:

        yes_no = input('Already have an account? Login !! ')

        if yes_no == 'yes':
            login()
            break

        elif yes_no == 'no':
            new_account()
            break


def login():
    global users
    # print(users)
    username = input("Username: ")

    with open('data.pickle', 'rb') as data:

        say = pickle.load(data)
        print(say)
        if username in say:
            password = input("Password: ")
            if users[username] == password:
                print('Logged in successfully. ')
            else:
                print("Please check your username and password !!")

        else:
            print('Invalid. ')


def new_account():
    global users

    new_user = input('Please enter a new username: ')

    with open('data.pickle', 'ab') as data:

        if new_user in users:
            print("That's already taken! Try another one.")

        else:
            new_pass = input("Please enter your new password: ")
            confirm = input("Confirm password: ")

            if new_pass == confirm:
                users[new_user] = new_pass
                pickle.dump(users, data)
                print('Successfully Created. ')
            else:
                print("password's don't match")


display()
print(users)
