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

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
