#import demo
import getpass

username = "jervy"
password = "123"

u = input("Enter your username: ")
p = getpass.getpass("Enter your password: ")  
if u == username and p == password:
    print("Access granted")
else:
    print("Access denied")