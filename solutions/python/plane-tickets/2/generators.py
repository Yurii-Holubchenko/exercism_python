"""Functions to automate Conda airlines ticketing system."""

SEAT_LETTERS = ("A", "B", "C", "D")
TICKET_NUMBER_LENGTH = 12

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    
    for counter in range(number):
        yield SEAT_LETTERS[counter % len(SEAT_LETTERS)]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    letters = generate_seat_letters(number)
    
    for counter in range(number):
        row = counter // len(SEAT_LETTERS) + 1
        if row >= 13:
            row += 1
        
        yield f"{row}{next(letters)}"


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    passengers_with_seats = {}
    seats = generate_seats(len(passengers))
    
    for passenger in passengers:
        passengers_with_seats[passenger] = next(seats)

    return passengers_with_seats


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """
    
    for seat_number in seat_numbers:
        base_str = f"{seat_number}{flight_id}"
        zeros_str = "0" * (TICKET_NUMBER_LENGTH - len(base_str))
        
        yield base_str + zeros_str
