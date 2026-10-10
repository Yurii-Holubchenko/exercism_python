def leap_year(year: int) -> bool:
    devided_by_4 = year % 4 == 0
    devided_by_100 = year % 100 == 0
    devided_by_400 = year % 400 == 0
    
    if devided_by_4 and not devided_by_100:
        return True
    elif devided_by_100 and devided_by_400:
        return True
    else:
        return False
