#elif

name = input("Enter your name ---> ")

age = int(input("Enter your age --->"))

if age >= 0 and age <= 5 :
	print("The age is considered as INFANT")

elif age >= 6 and age <= 12 :
	print("kid")

elif age >= 13 and age <= 19 :
	print("teenager")

elif age >= 20 and age <= 29 :
	print("Early Adulthood")

elif age >= 100 and age <= 101 :
	print("You're Too Old For My Program")

else:
	print("You're a Dinosaur")