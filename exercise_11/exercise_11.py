def getHoursMinutesSeconds(totalSecond):
    if totalSecond == 0:
        return "0s"
    if totalSecond < 60:
        return str(totalSecond) + "s"
    hour = 0
    minute = 0
    second = 0
    if totalSecond < 3600:
        minute = totalSecond // 60
        second = totalSecond - (minute * 60)
    if totalSecond >= 3600:
        hour = totalSecond // 3600
        minute = (totalSecond - (hour * 3600)) // 60
        second = totalSecond - (hour * 3600) - (minute * 60)
    time = []
    if hour > 0:
        time.append(str(hour) + "h")
    if minute > 0:
        time.append(str(minute) + "m")
    if second > 0:
        time.append(str(second) + "s")
    return " ".join(time)


def getDaysHoursMinutesSeconds(totalSecond):
    if totalSecond == 0:
        return "0s"
    if totalSecond < 60:
        return str(totalSecond) + "s"
    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    if totalSecond < 360:
        minutes = totalSecond // 60
        seconds = totalSecond - (minutes * 60)
    if totalSecond < 86400:
        hours = totalSecond // 3600
        minutes = (totalSecond - (hours * 3600)) // 60
        seconds = totalSecond - (hours * 3600) - (minutes * 60)
    else:
        days = totalSecond // 86400
        hours = (totalSecond - (days * 86400)) // 3600
        minutes = (totalSecond - (days * 86400) - (hours * 3600)) // 60
        seconds = totalSecond - (days * 86400) - (hours * 3600) - (minutes * 60)
    time = []
    if days > 0:
        time.append(str(days) + "d")
    if hours > 0:
        time.append(str(hours) + "h")
    if minutes > 0:
        time.append(str(minutes) + "m")
    if seconds > 0:
        time.append(str(seconds) + "s")
    return " ".join(time)


def main():
    print(getHoursMinutesSeconds(30))
    print(getHoursMinutesSeconds(60))
    print(getHoursMinutesSeconds(90))
    print(getHoursMinutesSeconds(3600))
    print(getHoursMinutesSeconds(3601))
    print(getHoursMinutesSeconds(3661))
    print(getHoursMinutesSeconds(0))

    print(getHoursMinutesSeconds(90042))
    print(getDaysHoursMinutesSeconds(90042))


if __name__ == "__main__":
    main()