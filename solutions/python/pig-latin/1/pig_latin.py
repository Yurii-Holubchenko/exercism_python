VOWELS = ("a", "e", "i", "o", "u")
SUFFIX = "ay"

def translate(text):
    words = []
    
    for word in text.split():
        if word.startswith(("xr", "yt", *VOWELS)):
            words.append(word + SUFFIX)
        else:
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
        
            words.append(word + SUFFIX)

    return " ".join(words)
