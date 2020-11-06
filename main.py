def binToDec():
  binary = input("Please enter a binary number: ")
  decNum = 0
  exp = 0
  counter = 1
  repeat = len(binary)
  while counter <= repeat:
      binD = binary[-1 * counter]
      decNum = decNum + int(binD) * 2 ** exp
      counter = counter + 1
      exp = exp + 1
  print(decNum)
  return decNum


def decToBin():
  binNumber = []
  remain = 0
  decNum = int(input("Please enter a Decimal number: "))
  while decNum != 0:
    remain = decNum%2
    decNum = int(decNum / 2)
    binNumber.insert(0,remain)
    if decNum == 1:
      binNumber.insert(0,1)
      break
  print(*binNumber, sep='')
  return binNumber

def hexToDec():
  decimal = []
    counter = 1
    repeat = len(hex)
    hex = input("Please enter a Hexidecimal number: ")
    hex = hex.upper()
    print(hex)
    for i in hex:
      if i == "1":
        decimal.insert(-1,1)
      elif i == "2":
        decimal.insert(-1,2)
      elif i == "3":
        decimal.insert(-1,3)
      elif i == "4":
        decimal.insert(-1,4)
      elif i == "5":
        decimal.insert(-1,5)
      elif i == "6":
        decimal.insert(-1,6)
      elif i == "7":
        decimal.insert(-1,7)
      elif i == "8":
        decimal.insert(-1,8)
      elif i == "9":
        decimal.insert(-1,9)
      elif i == "A":
        decimal.insert(-1,10)
      elif i == "B":
        decimal.insert(-1,11)
      elif i == "C":
        decimal.insert(-1,12)
      elif i == "D":
        decimal.insert(-1,13)
      elif i == "E":
        decimal.insert(-1,14)
      elif i == "F":
        decimal.insert(-1,15)

    for i in decimal:

    return







system = int(input("Please enter a number between 1 and 5: "))

if system == 1:
  binToDec()

elif system == 2:
  decToBin()

elif system == 3:
    hexToDec()
