def every15Minutes():
    for meridiem in ["am", "pm"]:
        for hour in ["12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
            for minute in ["00", "15", "30", "45"]:
                print(hour + ":" +minute + " " + meridiem)


def main():
    every15Minutes()


if __name__ == "__main__":
    main()