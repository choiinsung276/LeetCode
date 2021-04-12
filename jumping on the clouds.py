def jumpingOnClouds(c):
    jumpArr = {0}
    x = 0
    while True:

        if x == len(c) - 3 and c[x] == 0:
            jumpArr.add(x + 2)
            x += 2
            break
        if x == len(c) - 3 and c[x] == 1:
            jumpArr.add(x + 1)
            x += 1
            break

        if c[x + 1] == 1:
            jumpArr.add(x + 2)
            x += 2
            continue
        elif c[x + 1] == 0 and c[x + 2] == 1:
            jumpArr.add(x + 1)
            x += 1
            continue
        else:
            jumpArr.add(x + 2)
            x += 2
            continue

    return len(jumpArr) - 1

if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(str(result))