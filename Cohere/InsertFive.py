def solve(num):
    temp = str(num)
    ans = flost('-inf')
    for i in range(len(temp)+1):
        total = temp[:i] + '5' + temp[i:]
        if i == 0 and temp[0] == '-':
            continue
            ans = max(ans,int(total))
        return ans
