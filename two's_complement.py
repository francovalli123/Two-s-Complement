decimalNumber = int(input("Number: ")) # Enter a number in decimal system
decimalToBinary= bin(decimalNumber) 
binaryNumber = decimalToBinary[2:]

binaryNumber_toString = str(binaryNumber)
lenght = len(binaryNumber_toString)
array = [""] * lenght

for x in range(0,lenght):
    array[x] = int(binaryNumber_toString[x])

array = array[::-1]

for i in range(0, lenght):
    if array[i] == 1:
        j = i + 1
        if array[j] == 0:
            array[j] = 1
        else:
            array[j] = 0

twos_complement = ""

for k in range(0, lenght):
    twos_complement += str(array[k])

print(twos_complement) # Print the two's complement of the binary number