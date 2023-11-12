def convertToFahrenheit(degreesCelsius):
    fahrenheit = degreesCelsius * (9 / 5) + 32
    return fahrenheit


def convertToCelsius(degreeFahrenheit):
    celsius = (degreeFahrenheit - 32) * (5 / 9)
    return celsius


def main():
    print(convertToCelsius(0))
    print(convertToCelsius(180))
    print(convertToFahrenheit(0))
    print(convertToFahrenheit(100))
    print(convertToCelsius(convertToFahrenheit(15)))


if __name__ == "__main__":
    main()

