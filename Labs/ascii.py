# in order to make transmissions less readable, we devised a
# quick and simple encoding scheme:
# Encode: add a seed number to the ASCII value of each string.
# Decode: do the reverse, that is subtract the seed value, and print the decoded string

sentence = input('Enter sentence to be encoded:  ')

seed = int(input('Enter an integer encoding seed number between 5 and 20: '))
# make sure seed is between 5 and 20

def encode(uncoded_, seed_):
    coded = ''
    for ch in uncoded_:
        coded = coded + chr(ord(ch) + seed_)  # add seed to ASCII value for each character in sentence
    return coded


def decode(coded_, seed_):
    decoded = ''
    for ch in coded_:
        decoded = decoded + chr(ord(ch) - seed_)  # subtract seed to ASCII value for each encoded character in sentence
    return decoded


encoded_str = encode(sentence, seed)
print('Original string: ', sentence, seed)
print('Encoded string: ', encoded_str, seed)
print('Decoded string: ', decode(encoded_str, seed))
