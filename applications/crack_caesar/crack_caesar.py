# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

from collections import Counter, OrderedDict

"""
    NOTE TO SELF: You have to be in the directory itself in order for the open command to work. CD into the proper directory first, then try to run the text.

    PROBLEM: There's a large block of text in ciphertext.txt which I have no idea what it says. 
    
    SOLUTION: I need to develop a method for deciphering into plaintext from a ciphered text block by creating a hashmap which finds the most frequently used characters and then maps them to create a key.
    
    I can do this by analyzing the letter counts in the cipher text and then using the most frequently used letters in the mapped version and pairing them with the most frequently used letters in plaintext English.
    
    U - 
    P - 
        1) Implement a counter.
        2) Use a for loop to read the document. 
            2a) In the for loop, loop over every character and add it to the counter. Make sure to normalize the data all to uppercase or lowercase.
    E
    R

"""

letter_frequency = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
                    'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

most_common = []

# decode_table = {v: k for k, v in encode_table.items()}

# def encode(plain_text):
#     cipher = ""

#     for char in plain_text:
#         if char.isspace():
#             cipher += " "
#         else:
#             cipher += encode_table[char.upper()]
#     return cipher


# def decode(cipher_text):
#     cipher = ""

#     for char in cipher_text:
#         if char.isspace():
#             cipher += " "
#         else:
#             cipher += decode_table[char.upper()]
#     return cipher


# I am actually instantiating a dictionary here because I need to have both keys and values.

counted = Counter()

# define a helper function to define rules for the counter.


def build_counter(text):
    for char in text:
        if char.isspace():
            continue
        elif char not in letter_frequency:
            continue
        counted.update(char)

# define a helper function to create a new decoded message.


def crack_substitution(cipher, legend):
    decoded = ""

    for char in cipher:
        if char.isspace():
            decoded += " "
        elif char not in letter_frequency:
            decoded += char
        else:
            decoded += legend[char.upper()]
    return decoded


# open the text document up.
reader = open("ciphertext.txt", 'r')

# open a new document up with writing enabled.
writer = open("decipheredtext.txt", 'w')

# checking each line of text and using that line to fill out our counter.
for line in reader:
    build_counter(line)

reader.close()

# At this point, our counter has a list of all the keys in it with their appropriate letter counts.
# Next we create a list of the most common keys in the Counter.
for i, _ in counted.most_common():
    most_common.append(i)

# We combine that list with the pre-sorted list of letter frequencies in English to construct a key.
key = {most_common[i]: letter_frequency[i]
       for i in range(len(letter_frequency))}

reader = open('ciphertext.txt', 'r')

for line in reader:
    writer.write(crack_substitution(line, key))


reader.close()
writer.close()
