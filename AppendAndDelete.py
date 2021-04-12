def appendAndDelete(s, t, k):
    count = 0    #공통 문자수를 나타내는 count
    for i , j in zip(s,t):
        if i == j:
            count +=1
        else:
            break
    if count == 0:   #공통문자가 없는경우
        if len(s)+len(t)+1 <= k:    #지우는횟수 + 더하는횟수 + 1(빈문자열만들기)
            return "Yes"
        else:
            return "No"
    else:   #공통이 있는경우
        #두문자 모두 같은경우
        if (count == len(s)) and (count == len(t)):
            if 2*count+1<=k:
                return "Yes"
            else:
                return "No"
        elif len(s) - count + len(t) - count <= k: # s를 지우고 t문자 수를 더한다.
            return "Yes"
        else:
            return "No"

if __name__ == '__main__':


    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    print(result)