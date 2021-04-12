import itertools


def acmTeam(topic):
    maxcount = []  # 일의 개수
    result = []

    for t in itertools.combinations(topic, 2):
        count = 0
        for i in list(zip(t[0], t[1])):
            if '1' in i[0] or '1' in i[1]:
                count += 1

        maxcount.append(count)

    result.append(max(maxcount))  # 1의 개수중에 가장큰숫자
    result.append(maxcount.count(max(maxcount)))  # 가장큰숫자가 몇개있는지

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)
    print('\n'.join(map(str, result)))