VOWELS = ("a", "e", "i", "o", "u")

def translate(text):
    words = [_pig_latin(word) for word in text.split()]

    return " ".join(words)


def _pig_latin(word):
    if not word.startswith(("xr", "yt", *VOWELS)):
        initial_word = word
        
        for character in word:
            if character in VOWELS:
                if character == "u" and word[-1] == "q":
                    word = word[1:] + word[0]
                    continue

                break
            else:
                if character == "y" and not initial_word.startswith("y"):
                    break

                word = word[1:] + word[0]

    return word + "ay"
            