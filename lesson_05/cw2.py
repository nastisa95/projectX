# Complete the function which returns the weekday according to the input number.

def weekday(number: int) -> str:
    weekdays = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    return weekdays.get(number, "Wrong, please enter a number between 1 and 7")

number = int(input("Enter a number between 1 and 7: "))
print(weekday(number))
