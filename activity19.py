from getpass import getpass

isLogin = False
loginAttempt = 0

username = "123"
password = "321"

while isLogin == False:
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    if username == "123" and password == "321":
        print("Logged in!")
        print("Total login attempts: ", loginAttempt)
        loginAttempt += 1

    else:
        print("Username and password is incorrect. Please try again.")
        loginAttempt += 1
        isLogin = False