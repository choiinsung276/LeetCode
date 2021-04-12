import collections
def equalizeArray(arr):
    arrCount = collections.Counter(arr)
    return len(arr)-arrCount.most_common(1)[0][1]

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(str(result))