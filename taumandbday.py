def taumBday(b, w, bc, wc, z):
    # Write your code here
    if bc == wc:                             #흰색 검은색 금액 같은 경우
        return b*bc+w*wc
    elif bc != wc and bc < z and wc < z:     # 같지않은데 변환비용이 클때
        return b*bc+w*wc
    elif bc + z <= wc:                        # black비용이 더 작을때 다 검정으로사서 변환
        return bc*b + (bc+z)*w
    elif bc >= wc + z:                        # white 비용이 작을때 다 흰색사고 변환
        return w*wc + (wc+z)*b

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        print(str(result))

"""
10
384 887
2778 6916 7794
336 387
493 6650 1422
363 28
8691 60 7764
927 541
3427 9173 5737
212 369
2568 6430 5783
531 863
5124 4068 3136
930 803
4023 3059 3070
168 394
8457 5012 8043
230 374
4422 4920 3785
538 199
4325 8316 4371
"""
"""
result
7201244
906753
2841792
8134553
2917086
6231528
6197767
3395504
2857140
3981734
"""