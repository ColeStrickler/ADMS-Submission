


from collections import Counter
import sys
# Load instructions (reading from memory into registers)
load_instructions = [
    "lb",   # Load Byte (sign-extended)
    "lbu",  # Load Byte Unsigned (zero-extended)
    "lh",   # Load Halfword (sign-extended)
    "lhu",  # Load Halfword Unsigned (zero-extended)
    "lw",   # Load Word (32-bit)
    "lwu",  # Load Word Unsigned (zero-extended, RV64)
    "ld",   # Load Doubleword (64-bit, RV64)
    "flw",  # Load Floating-Point Word (32-bit float)
    "fld"   # Load Floating-Point Double (64-bit float)
]

# Store instructions (writing from registers into memory)
store_instructions = [
    "sb",   # Store Byte
    "sh",   # Store Halfword
    "sw",   # Store Word (32-bit)
    "sd",   # Store Doubleword (64-bit, RV64)
    "fsw",  # Store Floating-Point Word (32-bit float)
    "fsd"   # Store Floating-Point Double (64-bit float)
]


inst = load_instructions + store_instructions

def count_substrings(file_path, substrings):
    """
    Counts occurrences of specified substrings in a file.
    
    :param file_path: Path to the text file.
    :param substrings: List of substrings to count.
    :return: Dictionary with substring counts.
    """
    counts = Counter({substring: 0 for substring in substrings})
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            for substring in substrings:
                counts[substring] += line.count(substring)
    
    return counts

if __name__ == "__main__":
    fp = sys.argv[1]
    results_load = count_substrings(fp, load_instructions)
    results_store = count_substrings(fp, store_instructions)

    nloads = 0
    nstores = 0
    for substring, count in results_load.items():
        print(f"'{substring}' appears {count} times")
        nloads += count
    for substring, count in results_store.items():
        print(f"'{substring}' appears {count} times")
        nstores += count
    print(f"# Loads = {nloads}")
    print(f"# Stores = {nstores}")







