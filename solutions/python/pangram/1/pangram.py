LETTERS_IN_ALPHABET = 26

def is_pangram(sentence):
    letters = set(character for character in sentence.lower() if character.isalpha())
    
    return len(letters) == LETTERS_IN_ALPHABET
