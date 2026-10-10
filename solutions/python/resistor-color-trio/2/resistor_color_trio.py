COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

METRIC_PREFIX = ["", "kilo", "mega", "giga"]

def label(colors):
    color_1, color_2, color_3 = [COLORS[color] for color in colors[:3]]
    zeros = "0" * color_3
    numeric_value = int(f"{color_1}{color_2}{zeros}")
    multiplier_1000 = 0

    while numeric_value >= 1000:
        multiplier_1000 += 1
        numeric_value /= 1000
        
    return f"{numeric_value:g} {METRIC_PREFIX[multiplier_1000]}ohms"