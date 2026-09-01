from strength_check import check_strength
password=input("Enter the password: ")
score=check_strength(password)
print("Total Score: ",score)
