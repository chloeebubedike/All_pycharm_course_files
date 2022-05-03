import math
# year_book_written = 1950
year_input = input("What year is the book from? ")


def assign_century(year):
    century = int(year) / 100
    century_rounded_down = math.floor(century)
    return century_rounded_down + 1


def assign_decades(year):
    year_in_list = list(year)
    decade_number = int(year_in_list[-2])
    if decade_number == 9:
        return "Nineties"
    elif decade_number == 8:
        return "Eighties"
    elif decade_number == 7:
        return "Seventies"
    elif decade_number == 6:
        return "Sixties"
    elif decade_number == 5:
        return "Fifties"
    elif decade_number == 4:
        return "Fourties"
    elif decade_number == 3:
        return "Thirties"
    elif decade_number == 2:
        return "Twenties"
    elif decade_number == 1:
        return "Tens"
    elif decade_number == 0:
        return "Noughties"
    else:
        pass


century = assign_century(year_input)
decade = assign_decades(year_input)

print("{}th century, {}".format(century, decade))