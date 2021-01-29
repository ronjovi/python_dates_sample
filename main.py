# Roberto Sanchez, sanc735@usc.edu
# ITP 115, Spring 2021
# Lab 1

def main():
    # print out a rectangle( 2 wide -, 3 tall |)
    print(" __")
    print("|  |")
    print("|  |")
    print("|__|")

    # print out quote formatted
    print("\nYou don\'t frighten usm English pig-dogs!\nGo and boil your bottoms, sons of a silly person! \n         "
          "  - \"Monty Python and the Holy Grail\"")

    # ask user for day of week, month, then date #
    dayOfWeek = input("\nEnter the day of the week: ")  # input to get the day of the week (str)
    month = input("Enter the month: ")   # input to get the month (str)
    date = int(input("Enter the date: "))  # input to get the date, cast to int (int)

    # In order to deal with broken dates
    # we can do combination of if else statements
    # to check if we need to update the nextMonth and nextDate values
    # to the start of the next month

    lowercaseMonth = month.lower()  # first get lowercase month str, makes it easier to compare strings

    # checks if its last date in jan
    if lowercaseMonth == "january":
        if date == 31:
            nextDate = 1
            nextMonth = "february"

    # checks if its last date in feb
    elif lowercaseMonth == "february":
        if date == 28:
            nextDate = 1
            nextMonth = "march"

    # checks if its last date in march
    elif lowercaseMonth == "march":
        if date == 31:
            nextDate = 1
            nextMonth = "april"

    # checks if its last date in april
    elif lowercaseMonth == "april":
        if date == 30:
            nextDate = 1
            nextMonth = "may"

    # checks if its last date in may
    elif lowercaseMonth == "may":
        if date == 31:
            nextDate = 1
            nextMonth = "june"

    # checks if its last date in june
    elif lowercaseMonth == "june":
        if date == 30:
            nextDate = 1
            nextMonth = "july"

    # checks if its last date in july
    elif lowercaseMonth == "july":
        if date == 31:
            nextDate = 1
            nextMonth = "august"

    # checks if its last date in aug
    elif lowercaseMonth == "august":
        if date == 31:
            nextDate = 1
            nextMonth = "september"

    # checks if its last date in sept
    elif lowercaseMonth == "september":
        if date == 30:
            nextDate = 1
            nextMonth = "october"

    # checks if its last date in oct
    elif lowercaseMonth == "october":
        if date == 31:
            nextDate = 1
            nextMonth = "november"

    # checks if its last date in nov
    elif lowercaseMonth == "november":
        if date == 30:
            nextDate = 1
            nextMonth = "december"

    # checks if its last date in dec
    elif lowercaseMonth == "december":
        if date == 31:
            nextDate = 1
            nextMonth = "january"

    # if its not last day of any month
    else:
        nextMonth = month
        nextDate = date + 1

    # capitalize strings
    month = month.capitalize()
    nextMonth = nextMonth.capitalize()
    dayOfWeek = dayOfWeek.capitalize()

    print('\nToday is {}, {} {}. Tomorrow will be {} {}.'.format(dayOfWeek, month, date, nextMonth, nextDate))


main()
