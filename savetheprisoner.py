def saveThePrisoner(n, m, s):
    if m%n!=0:
        if s+m%n<=n:
            return s+(m%n)-1
        else:
            return s+(m%n)-1-n
    else:
        if s-1==0:
            return n
        else:
            return s-1

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        print(str(result))