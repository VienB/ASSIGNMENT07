# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# ouput: Valid

print("VIEN ANGELO BERNALES | BSCOE 1-1 \n")

InpPass = input("REGISTER YOUR PASSWORD: ")

user = InpPass
passLenght = len(user)
CapLetter = 0
Numbers = 0
SpecChac = 0

for AllNumbers in user:
    if AllNumbers in "1234567890":
        Numbers = Numbers + 1
        countNum = Numbers
    if Numbers == 0:
        countNum = 0

for NumCap in user:
    if NumCap in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        CapLetter = CapLetter + 1
        countCap = CapLetter
    if CapLetter == 0:
        countCap = 0

for SpecNum in user:
    if SpecNum not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        SpecChac = SpecChac + 1
        countSpec = SpecChac
    if SpecChac == 0:
        countSpec = 0

if passLenght > 15:
    CapValue = CapLetter
else:
    CapValue = 0

if CapValue>= 1:
    NumValue = Numbers
else:
    NumValue = 0

if NumValue >= 1:
    SpecValue = SpecChac
else:
    SpecValue = 0

if SpecValue >= 1:
    print("VALID!")
else:
    print("INVALID!")
    print("The password is valid if all criteria are met:")
    print("a. Greater than 15 letters")
    print("b. Have at least one capital letter")
    print("c. Have at least one number")
    print("d. Have at least one special char (!@#$%^&*()_+ etc)")
