def beautifulDays(i, j, k):
    days = [x for x in range(i,j+1)]
    count = 0
    for day in days:
        lday = str(day)[::-1].lstrip('0')
        result = abs(day-int(lday))/k
        if result.is_integer():
            count +=1
    return count

if __name__ == '__main__':
    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(str(result))