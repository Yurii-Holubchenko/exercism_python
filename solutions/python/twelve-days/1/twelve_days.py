DAYS = ("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth")
GIFTS = (
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
)

def recite(start_verse, end_verse):
    result_verse = []
    
    for row in range(start_verse, end_verse + 1):
        day = row - 1
        result_row = f"On the {DAYS[day]} day of Christmas my true love gave to me: "

        if row > 1:
            for day_gifts in GIFTS[day:0:-1]:
                result_row += day_gifts + ", "

            result_row += f"and {GIFTS[0]}"
        else:
            result_row += GIFTS[0]
        
        result_verse.append(result_row + ".")

    return result_verse