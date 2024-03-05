import random

pswrdLength = 4

nums = list(range(0,10))
chars = ['+','-','*','_','%','#','@','!','=','?']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
password = []

mustHaveMix = False
mustHaveLower = False
mustHaveUpper = False
mustHaveNums = False
mustHaveChars = False
charList = []

print('***********************************************************\nHi Welcome to password generator. Proceed to create your password')
pswrdLength = int(input("\nHow many charectors you want in your password?: "))
inp = input('\nDo you want your password to contain : \nEnter 1 for lowercase only alphabets\n Enter 2 for Capital letters only alphabet \n Enter 3 to mix both.: ')
if inp == '3': 
    mustHaveMix = True
    
elif inp == '2': 
    mustHaveLower = False
    mustHaveUpper = True

elif inp == '1': 
    mustHaveLower = True
    mustHaveUpper = False

inp = input('\nDo you want your password to include numbers?: Enter 1 for Yes OR 2 for No: ')
if inp == '1':
    mustHaveNums = True
elif inp == '2':
    mustHaveNums = False

inp = input('\nDo you want your password to include special charectors i.e @\n Enter 1 of Yes OR Enter 2 for No: ')
if inp == '1':
    mustHaveChars = True
elif input == '2':
    mustHaveChars = False

if mustHaveMix and mustHaveNums and mustHaveChars:
    charList = nums + chars + alphabet + upperAlpha

elif mustHaveMix and mustHaveNums:
    charList = alphabet + upperAlpha + nums

elif mustHaveMix and mustHaveChars:
    charList = alphabet + upperAlpha + chars

elif mustHaveLower and mustHaveNums and mustHaveChars:
    charList = alphabet + nums + chars

elif mustHaveLower and mustHaveNums:
    charList = alphabet + nums

elif mustHaveLower and mustHaveChars:
    charList = alphabet + chars

elif mustHaveUpper and mustHaveNums and mustHaveChars:
    charList = alphabet + nums + chars

elif mustHaveUpper and mustHaveNums:
    charList = upperAlpha + nums

elif mustHaveUpper and mustHaveChars:
    charList = upperAlpha + chars



def generate(a):
    password1 = []
    while len(password1) < pswrdLength:
        randIndex = random.randint(0, len(charList)-1)
        password1.append(str(charList[randIndex]))
    return password1



password = generate(charList)
# password = list(password)
password = ''.join(password)



print('\n\nYour PASSWORD is: ' + password)

