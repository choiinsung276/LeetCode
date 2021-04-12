# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def migratoryBirds(arr):
    result = {}
    for ar in arr:
        if ar in result:
            result[ar] += 1
        else:
            result[ar] = 1
    result = sorted(result.items(), key =lambda x:x[1], reverse=True)
    return result[0][0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(str(result))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
