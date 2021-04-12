def pageCount(n, p):
    front = p/2
    back = n/2-p/2
    return int(min(front,back))
if __name__ == '__main__':
    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(str(result))