# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

from collections import Counter

"""
    NOTE TO SELF: You have to be in the directory itself in order for the open command to work. CD into the proper directory first, then try to run the text.

    U - 
    
        PROBLEM: There's a large block of text in ciphertext.txt which I have no idea what it says. 
        
        SOLUTION: I need to develop a method for deciphering into plaintext from a ciphered text block by creating a hashmap which finds the most frequently used characters and then maps them to create a key.
        
        I can do this by analyzing the letter counts in the cipher text and then using the most frequently used letters in the mapped version and pairing them with the most frequently used letters in plaintext English.
    
    P - 
        1) Implement a counter.
        2) Use a for loop to read the document. 
            2a) In the for loop, loop over every character and add it to the counter. Make sure to normalize the data all to uppercase or lowercase.
            2b) A counter will order items in descending order. I have to pull the keys out of that counter while preserving the order so that all of the most common letters appear in the correct order.
        3) Create a decryption key by pairing the most frequently used letters in the cipher with the most frequently used letters in English.
        4) Run back through the ciphered document, this time using the key to filter the ciphered text and outputting the result to another txt document.
        
    E - See program below.
    
    R - Program was created very declaratively. I built helper functions, but I'm wondering if I can do it all 
        in place.

"""

letter_frequency = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
                    'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

most_common = []

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

    decoded += "\n"
    return decoded


# open the text document up.
reader = open("ciphertext.txt", 'r')

# open a new document up with writing enabled.
writer = open("decipheredtext.txt", 'w')

# checking each line of text and using that line to fill out our counter.
for line in reader:
    build_counter(line)

# close the text document.
reader.close()

# At this point, our counter has a list of all the keys in it with their appropriate letter counts.
# Next we create a list of the most common keys in the Counter.
for i, _ in counted.most_common():
    most_common.append(i)

# We combine that list with the pre-sorted list of letter frequencies in English to construct a key.
key = {most_common[i]: letter_frequency[i]
       for i in range(len(letter_frequency))}

# We now have a key which pairs the most commonly occurring characters in the ciphered text with the most commonly occuring characters in plaintext English.

# open the reader again.
reader = open('ciphertext.txt', 'r')

# for some reason it didn't like it when I just kept the reader open before, so we'll re-open the reader.
for line in reader:
    writer.write(crack_substitution(line, key))


# Closing both of the open files.
reader.close()
writer.close()

# Success.
