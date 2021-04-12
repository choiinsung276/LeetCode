def repeatedString(s, n):
    findIndex = []
    count = 0
    for i, x in enumerate(s):
        if x == 'a':
            findIndex.append(i)

    for i in findIndex:
        count += n // len(s) - 1
        if i <= n % len(s):
            count += 1

    return count

if __name__ == '__main__':


    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(str(result))