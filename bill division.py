def bonAppetit(bill, k, b):
    sum_b = sum(bill) - bill[k]
    if b-sum_b>0:
        print(b-sum_b)
    else:
        print("Bon Appetit")
if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
