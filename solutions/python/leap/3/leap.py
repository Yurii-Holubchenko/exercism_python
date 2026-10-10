def leap_year(year: int) -> bool:
    """Function, which check is the year is the leap year or not

    Parameters:
        year (int): The year for determination.

    Returns:
        bool: The result of the determination whether the year is leap or not

    Examples:
        >>> leap_year(40)
        True

        >>> leap_year(300)
        False
    """
    
    devided_by_4 = year % 4 == 0
    devided_by_100 = year % 100 == 0
    devided_by_400 = year % 400 == 0
    
    if devided_by_4 and not devided_by_100:
        return True
    
    if devided_by_100 and devided_by_400:
        return True
    
    return False
