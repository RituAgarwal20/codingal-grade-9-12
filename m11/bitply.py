# 01-bits-and-binary.py
# Topic: Bits and Binary Numbers, AND and OR

n = int(input("Enter a number (try 5 or 12): "))
guess = input("Guess its binary: ")

input("Binary.  Press Enter ")
print("  decimal", n, "->  binary", bin(n)[2:])
print("  your guess:", guess)

input("AND — both bits must be 1.  Press Enter ")
print("  12 =", bin(12)[2:])
print("  10 =", bin(10)[2:])
print("  12 & 10 =", 12 & 10)

input("OR — at least one bit must be 1.  Press Enter ")
print("  12 | 10 =", 12 | 10)




# 02-not-xor-shifts.py
# Topic: NOT, XOR, Left Shift, Right Shift

n = int(input("Enter a number (try 5 or 12): "))
guess = input("Left shift doubles it. Guess: " + str(n) + " << 1 = ? ")

input("NOT — flips every bit.  Press Enter ")
print("  12 =", bin(12)[2:])
print("  NOT 12 =", ~12 & 0xFF)

input("XOR — different bits give 1.  Press Enter ")
print("  12 ^ 10 =", 12 ^ 10)

input("Left shift — multiplies by 2.  Press Enter ")
print("  ", n, "<< 1 =", n << 1, "  your guess:", guess)

input("Right shift — divides by 2.  Press Enter ")
print("  ", n, ">> 1 =", n >> 1)


# 03-parity-bits.py
# Topic: Parity Check and Counting Bits

input("Parity — last bit = 0 even,  last bit = 1 odd.  Press Enter ")
for n in [2, 3, 4, 5, 8, 9]:
    if n & 1:
        print("  ", n, "->  odd")
    else:
        print("  ", n, "->  even")

n = int(input("Enter a number (try 13 or 7): "))
input("Count the 1s — watch bits drop off.  Press Enter ")
temp = n
while temp > 0:
    print("  binary:", bin(temp)[2:], "  last bit:", temp & 1)
    temp >>= 1
print("  total 1s in", n, "=", bin(n).count('1'))