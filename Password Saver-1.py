import csv
import sys


passwords = [["yahoo","XqffoZeo"],["google","CoIushujSetu"]]


passwordFileName = "samplePasswordFile"

encryptionKey=16

def passwordEncrypt (unencryptedMessage, key):

    encryptedMessage = ''


    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol

    return encryptedMessage

def loadPasswordFile(fileName):

    with open(fileName, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)

    return passwordList

def savePasswordFile(passwordList, fileName):

    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)



while True:
    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Lookup a password")
    print(" 3. Add a password")
    print(" 4. Save password file")
    print(" 5. Print the encrypted password list (for testing)")
    print(" 6. Quit program")
    print("Please enter a number (1-4)")
    choice = input()

    if(choice == '1'):
        passwords = loadPasswordFile(passwordFileName)

    if(choice == '2'):
        print("Which website do you want to lookup the password for?")
        for keyvalue in passwords:
            print(keyvalue[0])
        passwordToLookup = input()

    for i in range(len(passwords)):
            if passwordToLookup in passwords[i][0]:
                print(loadPasswordFile([i][0]))
            if passwordToLookup == website:
                print(passwords)





    if(choice == '3'):
        print("What website is this password for?")
        website = input()
        print("What is the password?")
        unencryptedPassword = input()

        encryptedPassword = passwordEncrypt(unencryptedPassword,encryptionKey)


    if(choice == '4'):
            savePasswordFile(passwords,passwordFileName)


    if(choice == '5'):
        for keyvalue in passwords:
            print(', '.join(keyvalue))

    if(choice == '6'):
        sys.exit()

    print()
    print()
