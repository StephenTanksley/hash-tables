# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

from collections import Counter

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

punctuation = ['!', '(', ')', '-', '[', ']', '{', '}', ';', ':', ',', '"',
               "'", '<', '>', '.', '/', '?', '@', '#', '$', '%', '^', '&', '*', '_', '~']


with open("ciphertext.txt", 'r') as reader:
    for line in reader:
        print(line, end="")

c = Counter()


def build_key(text):
    for char in text:
        if char.isspace():
            continue
        elif char in punctuation:
            continue
        else:
            c.update(char)


build_key(reader)
print(c)


def crack_substitution(text):
    pass


reader.close()
