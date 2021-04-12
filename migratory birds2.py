import collections


def migratoryBirds(arr):
    result = collections.Counter(arr)
    return result.most_common(1)[0][0]

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(str(result))