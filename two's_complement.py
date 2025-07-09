decimalNumber = int(input("Number: "))  # Ingresa un número decimal

# Si es positivo, simplemente mostramos el binario sin el '0b' prefix
if decimalNumber >= 0:
    binary = bin(decimalNumber)[2:]
    print(binary)

else:
    # Si es negativo, obtenemos el complemento a dos del valor absoluto
    abs_value = abs(decimalNumber)
    binary = bin(abs_value)[2:]  # binario del valor absoluto
    length = len(binary)

    # Aseguramos un tamaño fijo (por ejemplo, 8 bits)
    fixed_length = max(8, length)
    binary = binary.zfill(fixed_length)

    # Invertimos los bits (complemento a uno)
    inverted = ''.join('1' if bit == '0' else '0' for bit in binary)

    # Sumamos 1 para obtener el complemento a dos
    inverted_list = list(inverted)
    carry = 1
    for i in range(len(inverted_list) - 1, -1, -1):
        if inverted_list[i] == '1' and carry == 1:
            inverted_list[i] = '0'
        elif inverted_list[i] == '0' and carry == 1:
            inverted_list[i] = '1'
            carry = 0

    twos_complement = ''.join(inverted_list)
    print(twos_complement)
