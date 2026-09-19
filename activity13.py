import getpass
(input('Input First Name :'))
(input('Input Last Name :'))
(input('Job Title :'))

username = "jervy"
password = "123"

u = input("Enter your username: ")
p = getpass.getpass("Enteryour password: ")
if u == username and p == password:
    print("******Access granted******")
else:
    print("******Access denied******")

input("\n Type of Collateral to use : ")
collateral = float(input("\n Value of Collateral : "))

if collateral < 30000:
    print("Collateral is not enough to secure a loan")
else:
    print("\n Congratulations! You're Collateral is enough to secure a loan")

age=int(input("\n Input your age : "))

base_rate = 0.0
if age >= 21 :
    print('******Passed baseline eligibility criteria******')
else:
    print('******You are underage******')

job=str(input("\n Input do you have a job? (yes/no) : "))   
if job == "yes":
    print('******Nice Job!******')
else:
     print('******Get a job buddy******')

credit_score=int(input("\n Input your credit score : "))

if credit_score >= 750:
    print('******Your credit score is above 750******')
else:
        print('******Your credit score is below 750******')

income=float(input("\n How much is your annual income?  "))

if income >= 100000:
    base_rate = 4.5
    print('******You Have High Income******')
else:
     base_rate = 5.0
print('Your interest rate is', base_rate)
    

