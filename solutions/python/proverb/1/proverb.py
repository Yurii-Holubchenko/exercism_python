def proverb(*input_data, qualifier=None):
    if not input_data:
        return []
    
    lines = [
        f"For want of a {first} the {second} was lost."
        for first, second in zip(input_data, input_data[1:])
    ]    
    last_row_word = f"{qualifier} {input_data[0]}" if qualifier else input_data[0]

    return [*lines, f"And all for the want of a {last_row_word}."]
    