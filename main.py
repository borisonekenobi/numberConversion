def binToDec(binary):
    decNum = 0
    exp = 0
    counter = 1
    repeat = len(binary)
    while counter <= repeat:  # counter uses the length to make the Decimal number
        binD = binary[-1 * counter]
        decNum = decNum + int(binD) * 2 ** exp
        counter = counter + 1
        exp = exp + 1
    return decNum


def decToBin(decNum):
    binNumber = []
    remain = 0
    while decNum != 0:  # checks if the Decimal number has reached 0
        remain = decNum % 2  # checking for 0 or 1 remainder
        decNum = int(decNum / 2)  # divides Decimal by 2
        binNumber.insert(0, remain)
        if decNum == 1:
            binNumber.insert(0, 1)
            break
    return binNumber


def hexToDec(hexNum):
    hexNum = hexNum.upper()  # ensures all the letters are capitalized
    exp = len(hexNum) - 1
    sum = 0
    for i in hexNum:  # converts the corresponding letters to numbers
        if i == 'A':
            i = 10
        if i == 'B':
            i = 11
        if i == 'C':
            i = 12
        if i == 'D':
            i = 13
        if i == 'E':
            i = 14
        if i == 'F':
            i = 15
        sum = sum + int(i) * 16 ** exp  # does the exponent and multiplication
        exp = exp - 1
    return sum


def decToHex(decNum):
    hexNumber = []
    remain = 0
    while decNum != 0:  # checks if the Decimal number has reached 0
        remain = decNum % 16
        decNum = int(decNum / 16)  # divides Decimal by 16
        hexNumber.insert(0, remain)
        if decNum == 1:
            hexNumber.insert(0, 1)
            break
        for i in range(0, len(hexNumber)):
            if hexNumber[i] == 10:
                hexNumber[i] = "A"
            if hexNumber[i] == 11:
                hexNumber[i] = "B"
            if hexNumber[i] == 12:
                hexNumber[i] = "C"
            if hexNumber[i] == 13:
                hexNumber[i] = "D"
            if hexNumber[i] == 14:
                hexNumber[i] = "E"
            if hexNumber[i] == 15:
                hexNumber[i] = "F"

    return hexNumber


def hexToBin(hexNum):
    decNum = hexToDec(hexNum)
    binNum = decToBin(decNum)
    return binNum


print("Please enter the following options:", end='\n\n')
print("Enter 1 for converting Binary to Decimal", end='\n\n')
print("Enter 2 for converting Decimal to Binary", end='\n\n')
print("Enter 3 for converting Hexadecimal to Decimal", end='\n\n')
print("Enter 4 for converting Decimal to Hexadecimal", end='\n\n')
print("Enter 5 for converting Hexadecimal to Binary", end='\n\n')
print("Any other number to exit", end='\n\n')
while True:
    system = int(input("Please enter a number between 1 and 5: "))

    if system == 1:
        binary = input("Please enter a binary number: ")
        print(binToDec(binary))

    elif system == 2:
        decNum = int(input("Please enter a Decimal number: "))
        print(*decToBin(decNum), sep='')

    elif system == 3:
        hexNum = input("Please enter a Hexadecimal number: ")
        print(hexToDec(hexNum))

    elif system == 4:
        decNum = int(input("Please enter a Decimal number: "))
        print(*decToHex(decNum), sep='')

    elif system == 5:
        hexNum = input("Please enter a Hexadecimal number: ")
        print(*hexToBin(hexNum), sep='')

    else:
        break
