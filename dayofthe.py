import datetime
import time

def dayOfProgrammer(year):
    a = datetime.datetime(year,1,1)-datetime.datetime(year,9,1)
    b = abs(a).days
    sub = 256 - b
    result = datetime.datetime(year,9,sub).strftime('%d.%m.%Y')
    return result


if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)
    print(result)