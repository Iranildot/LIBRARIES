from csv import *
from random import shuffle
from os import mkdir
from search import *

def encryptPassword(password:str, key:list, converter:list, repeat:int):
    # Preparing string to encrypt
    aux = []
    for character in password:
        aux.append(character)

    # Encrypting message
    counter = 0 
    while counter < repeat:
        for i in range(len(aux)):
            j = linear(key, ord(aux[i])*" ")
            if j >= 0:
                aux[i] = chr(len(converter[j]))
        
        counter += 1

    password = ""
    for character in aux:
        password += character
    return password

def decryptPassword(password:str, key:list, converter:list, repeat:int):
    # Preparing string to encrypt
        aux = []
        for character in password:
            aux.append(character)

        # Decrypting message
        counter = 0
        while counter < repeat:
            for i in range(len(aux)):
                j = binary(converter, ord(aux[i])*" ")
                if j >= 0:
                    aux[i] = chr(len(key[j]))
            
            counter += 1

        password = ""
        for character in aux:
            password += character
        return password

def createKeys(password:str):
    repeat = 0
    for number in password:
        repeat += int(number)

    key = []
    motherKey = []
    converter = []

    # Gera motherkey
    i = 48
    while (i < 123):
        if i == 91:
            i = 97
        converter.append(" "*i)
        motherKey.append(" "*i)
        key.append(" "*i)
        i += 1
    
    # Gera valores aleatórios para key e motherKey
    while key == motherKey:
        shuffle(motherKey)
        shuffle(key)
    

    for item in key:
        print(chr(len(item)), end="")
    print()

    password = encryptPassword(password, key, converter, repeat)

    # Encrypting key
    counter = 0
    while counter < repeat:
        for i in range(len(key)):
            j = linear(motherKey, key[i])
            key[i] = converter[j]
        counter += 1
    
    # Encrypting motherKey
    counter = 0
    while counter < repeat:
        for i in range(len(motherKey)):
            j = linear(key, motherKey[i])
            motherKey[i] = converter[j]
        
        counter += 1

    with open("./.keys/key.txt", "w") as file:
        for item in key:
            file.write(item)
            file.write("\n")

    with open("./.keys/motherKey.txt", "w") as file:
        for item in motherKey:
            file.write(item)
            file.write("\n")
    
    with open("./.keys/converter.txt", "w") as file:
        for item in converter:
            file.write(item)
            file.write("\n")
    
    with open("./.keys/password.txt", "w") as file:
        file.write(password)

def encrypt(message, password:int):
    message = str(message)
    password = str(password)

    key = []
    motherKey = []
    converter = []

    repeat = 0
    for number in password:
        repeat += int(number)
    
    storedPassword = ""

    try:
        
        # Opening files
        with open("./.keys/key.txt", "r") as file:
            for item in reader(file):
                key.append(item[0])
        
        with open("./.keys/motherKey.txt", "r") as file:
            for item in reader(file):
                motherKey.append(item[0])
            
        with open("./.keys/converter.txt", "r") as file:
            for item in reader(file):
                converter.append(item[0])
        
        with open("./.keys/password.txt", "r") as file:
            for item in reader(file):
                storedPassword = item[0]
        
        # Decrypting motherKey
        counter = 0
        while counter < repeat:
            for i in range(len(motherKey)):
                j = binary(converter, motherKey[i])
                motherKey[i] = key[j]
            
            counter += 1
        
        # Decrypting key
        counter = 0
        while counter < repeat:
            for i in range(len(key)):
                j = binary(converter, key[i])
                key[i] = motherKey[j]
            
            counter += 1
        
       
        storedPassword = decryptPassword(storedPassword, key, converter, repeat)
        
        if storedPassword == password:

            # Preparing string to encrypt
            aux = []
            for character in message:
                aux.append(character)

            # Encrypting message
            counter = 0
            while counter < repeat:
                for i in range(len(aux)):
                    j = linear(key, ord(aux[i])*" ")
                    if j >= 0:
                        aux[i] = chr(len(converter[j]))
                
                counter += 1

            message = ""
            for character in aux:
                message += character

            return message

        else:
            print("Wrong password!")
            return "ERROR 1"

    except:

        try:
            mkdir("./.keys/")
            createKeys(password)
            print("Creating needed folder and files.")
        except:
            createKeys(password)
            print("Creating needed files.")

        return 1

def decrypt(message, password:int):
    message = str(message)
    password = str(password)

    key = []
    motherKey = []
    converter = []

    repeat = 0
    for number in password:
        repeat += int(number)

    storedPassword = ""

    try:
        # Opening files
        with open("./.keys/key.txt", "r") as file:
            for item in reader(file):
                key.append(item[0])
        
        with open("./.keys/motherKey.txt", "r") as file:
            for item in reader(file):
                motherKey.append(item[0])
            
        with open("./.keys/converter.txt", "r") as file:
            for item in reader(file):
                converter.append(item[0])
        
        with open("./.keys/password.txt", "r") as file:
            for item in reader(file):
                storedPassword = item[0]


        # Decrypting motherKey
        counter = 0
        while counter < repeat:
            for i in range(len(motherKey)):
                j = binary(converter, motherKey[i])
                motherKey[i] = key[j]
            
            counter += 1
        
        # Decrypting key
        counter = 0
        while counter < repeat:
            for i in range(len(key)):
                j = binary(converter, key[i])
                key[i] = motherKey[j]
            
            counter += 1

        
        storedPassword = decryptPassword(storedPassword, key, converter, repeat)
        
        if storedPassword == password:

            # Preparing string to decrypt
            aux = []
            for character in message:
                aux.append(character)

            # Decrypting message
            counter = 0
            while counter < repeat:
                for i in range(len(aux)):
                    j = binary(converter, ord(aux[i])*" ")
                    if j >= 0:
                        aux[i] = chr(len(key[j]))
                
                counter += 1

            message = ""
            for character in aux:
                message += character
            
            return message
        
        else:
            print("Wrong password!")
            return "ERROR 1"

    except:

        try:
            mkdir("./.keys/")
            createKeys(password)
            print("Creating needed folder and files.")
        except:
            createKeys(password)
            print("Creating needed files.")

        return 1
