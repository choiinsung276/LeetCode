import collections


def sockMerchant(n, ar):
    result = collections.Counter(ar)
    count = 0
    for i in result.values():
        if i<2:
            continue
        else:
            count += i//2

    return count

if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result))

