"""
    Problem: We want to remove duplicate words. If a word happens more than once in a string, we want to ignore the subsequent repetitions of that word. i.e. "hello hello" becomes "hello"
    
    Solution: We can use a set here. Set is a sub-class of dict which only takes keys. Since we only need the keys, we don't need to push a value to the set. 
    
    We'll split the original string into separate words and then we'll join them based on a sorted set. We'll use a key of words.index to determine the order in which the words are joined to the final return string.

"""


def no_dups(s):

    # Split the string into separate words.
    words = s.split()

    # Sort the list of words by sorting the set they've been inserted into using the index of where they appear in the words list.
    sorted_words = sorted(set(words), key=words.index)

    # Join those words together to form a string with a " " as a separator.
    return_string = (" ".join(sorted_words))

    return return_string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
