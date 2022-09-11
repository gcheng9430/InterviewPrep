def solution(temp):
    n = len(temp)
    # set up the prefix sum list
    prefix = [temp[0] for _ in range(n)]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + temp[i]

    res = max(prefix[0], prefix[-1])

    # iterate and compare
    for i in range(1, n):
        res = max(res, max(prefix[i], prefix[n-1]-prefix[i-1]))
    return res

def main():
    temp = [6, -2, 5] 
    ans = solution(temp)
    print(ans)

if __name__ == "__main__":
    main()