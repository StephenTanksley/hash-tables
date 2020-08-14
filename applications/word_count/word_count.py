"""
    Problem: We have a string which we need to determine word count in. We need to use a dictionary to solve this problem.
    
    Solution: 
        1) First, I think the punctuation should be removed entirely. 
        2) Then we can use the resulting clean string create a dictionary with { word : count}.
            2a) All of the keys need to appear lowercase in the dictionary.
            2b) Key order doesn't matter as long as everything shows up.
        3) Return the dictionary.

"""

# import collections

punctuation = ['"', ':', ';', ',', '.',  '-', '+', '=', '/',
               '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']


def word_count(s):

    split = s.split()

    words = ["".join(char.lower() for char in word if char.isalpha()
                     or char not in punctuation) for word in split]

    # dict comprehension which creates a table by looping through words and uses {key (i): and count(i) for each word in the words list.}

    table = {word: words.count(word) for word in words if word != ""}

    return table


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
