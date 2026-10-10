def response(hey_bob):
    hey_bob = hey_bob.strip()
    is_upper = hey_bob.isupper()
    is_question = hey_bob.endswith("?")
    
    if hey_bob == "":
        return "Fine. Be that way!"
    
    if is_upper and is_question:
        return "Calm down, I know what I'm doing!"
    
    if is_question:
        return "Sure."

    if is_upper:
        return "Whoa, chill out!"

    return "Whatever."
    
