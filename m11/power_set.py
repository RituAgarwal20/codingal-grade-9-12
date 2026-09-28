# 01-power-set.py
# Topic: Power Set, Binary Mask as a Subset Selector

input("A set with n elements has 2^n subsets.  Press Enter ")
print("  3 elements  2^3 =", 2**3, "subsets")
print("  mask 5 = binary", bin(5)[2:], "  selects positions 0 and 2")

n = int(input("Enter number of elements (try 4 or 5): "))
guess = input("How many subsets does a set of " + str(n) + " elements have? ")
input("Each element is in or out - 2 choices per element.  Press Enter ")
print(" ", n, "elements  subsets:", 2**n, "  your guess:", guess)



# 02-bit-probe.py
# Topic: Bit Probe - Checking the j-th Bit, Enumerating All Subsets with Two Loops

input("Bit probe - (n >> j) & 1 checks if bit j is ON.  Press Enter ")
print("  12 = binary", bin(12)[2:], "  bit 2:", (12 >> 2) & 1, "  bit 1:", (12 >> 1) & 1)
print("  7  = binary", bin(7)[2:],  "  bit 2:", (7 >> 2) & 1,  "  bit 1:", (7 >> 1) & 1)

n = int(input("Enter a number (try 9 or 6): "))
print("  binary:", bin(n)[2:])
guess = input("What is bit 2 of " + str(n) + "? (0 or 1): ")
input("Bit probe: (n >> 2) & 1 gives the bit value.  Press Enter ")
print(" ", n, "bit 2 =", (n >> 2) & 1, "  your guess:", guess)