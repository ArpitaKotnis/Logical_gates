def and_gate(a, b):
    return a & b

def or_gate(a, b):
    return a | b

def not_gate(a):
    return 1 - a

def xor_gate(a, b):
    return a ^ b

def nand_gate(a, b):
    return 1 - (a & b)

def nor_gate(a, b):
    return 1 - (a | b)

def binary_gate_finder(a, b=None):
    if b is not None:
        print(f"AND Gate: {and_gate(a, b)}")
        print(f"OR Gate: {or_gate(a, b)}")
        print(f"XOR Gate: {xor_gate(a, b)}")
        print(f"NAND Gate: {nand_gate(a, b)}")
        print(f"NOR Gate: {nor_gate(a, b)}")
    print(f"NOT Gate (a): {not_gate(a)}")
    if b is not None:
        print(f"NOT Gate (b): {not_gate(b)}")

# Example usage
a = int(input("Enter the first binary input (0 or 1): "))
b = int(input("Enter the second binary input (0 or 1), or press Enter to skip: ") or None)

binary_gate_finder(a, b)
