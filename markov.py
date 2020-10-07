"""Generate Markov text from text files."""
import random
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    input_file = open(file_path)
    return input_file.read()

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    word_list = text_string.split() 
    chains = {}

    for i in range(len(word_list) - 2):
        # loop through each item on the word_list, that has now been split
        key_tuple = (word_list[i], word_list[i + 1])
        # create a tuple of word_list[i] and the next word and store it in key_tuple
        if key_tuple not in chains.keys():
            #if this tuple pairing is not in the keys of chains dictionary, then add it, 
            # along with the corresponding values that would go after the digrams in 
            # text file
            chains[key_tuple] = [word_list[i + 2]]
        else:
            # add the element of word_list[i + 2] as a value to the key
            chains[key_tuple].append(word_list[i + 2])
    
    return chains

def make_text(chains):
    """Return text from chains."""
    # Would you like them Sam I am?
    #('Would', 'you'): ['could', 'could', 'could', 'could', 'like', 'like']
    #randomize to get first_tuple, then add to words[] list
    #find corresponding values
    #randomize on those values
    words = []




    return ' '.join(words)


# def test_function(input_text):
#     input_text = "Happy Tuesday Morning"
#     input_text_list = input_text.split()
#     for i in range(len(input_text_list) - 1): # range(2) ->  0 , 1
#         print(input_text_list[i], input_text_list[i+1])

input_path = 'green-eggs.txt'
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
#open_and_read_file('green-eggs.txt')
#test_function(input_text)
# Get a Markov chain
chains = make_chains(input_text)
# Produce random text
random_text = make_text(chains)

print(random_text)

#pt2
    # chains = {}
    # word_list = text_string.split()
    # for i in range(len(word_list) - 2):
    #     key_tuple = (word_list[i], word_list[i + 1])
    #     if key_tuple not in chains.keys():
    #         chains[key_tuple] = [word_list[i + 2]]
    #     else:
    #         chains[key_tuple].append(word_list[i + 2])
    
    # return chains

# pt 3
    # keys_list = list(chains.keys())
    # random_word = (random.choice(keys_list))
    # words = [random_word[0], random_word[1]]
    # next_word = random.choice(chains[random_word]) # randomize value
    # words.append(next_word)


    # new_tuple = (words[-2], words[-1])
    # print(f"The link {words}")
    # print (f" Keys List : {keys_list}")
    # while new_tuple in keys_list:
    #     print(f"Tuple after entering loop {new_tuple}")
    #     next_word = random.choice(chains[new_tuple])
    #     print(f"next word is - {next_word}")
    #     words.append(next_word)
    #     print(f"Word list after adding {words}")
    #     new_tuple = (words[-2], words[-1])
    #     print(f"Tuple end of loop {new_tuple}")