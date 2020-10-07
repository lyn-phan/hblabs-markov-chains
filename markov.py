"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    #open green-eggs-ham file
    #file.read to open as a string
    #return the string
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
    # word_list = split the text_string on blankspace

    # define a dictionary bigram_dict
    # Loop through word_list 
    # for i in range(len(word_list) - 1): 0 to 2
    # if (word_list[i], word_list[i + 1]) is not found in the key,
        #make a tuple of  (word_list[i], word_list[i + 1]) and insert it as key in bigram_dict
        # add the elemen in word_list[i + 2] as a value to the key
    #else 
        # add the elemen in word_list[i + 2] as a value to the key

    # bigram_dict= {("Happy", "Tuesday") : [Morning, Evening]}
    
    chains = {}
    word_list = text_string.split()
    for i in range(len(word_list) - 2):
        key_tuple = (word_list[i], word_list[i + 1])
        if key_tuple not in chains.keys():
            chains[key_tuple] = [word_list[i + 2]]
        else:
            chains[key_tuple].append(word_list[i + 2])
    
    return chains

def make_text(chains):
    """Return text from chains."""

    words = [] # Would you like them Sam I am?
    #('Would', 'you'): ['could', 'could', 'could', 'could', 'like', 'like']
    #randomize to get first_tuple, then add to words[] list
    #find corresponding values
    #randomize on those values
    #

    ('I','am?') 
    # your code goes here

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
