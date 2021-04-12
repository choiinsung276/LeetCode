def nonDivisibleSubset(k, S):
    S_remainder = [s % k for s in S]  # 리스트에 포함된 모든 정수를 k로 나눈 나머지 계산
    result = 0  # 부분집합의 크기

    for i in range(1, k // 2 + 1):  # (1, k-1), (2, k-2), ... 순회
        if i != k - i:
            # i를 나머지로 갖는 정수들과 k-i를 나머지로 갖는 정수들 중 더 많은 쪽을 포함시킴.
            result += max(S_remainder.count(i), S_remainder.count(k - i))
        else:
            # k로 나눈 나머지가 k//2인 정수가 있는지 확인하여 하나만 포함시킴.
            result += int(bool(S_remainder.count(i)))

    result += int(bool(S_remainder.count(0)))  # k로 나눈 나머지가 0인 정수가 있는지 확인하여 하나만 포함시킴.

    return result

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)
    print(str(result))