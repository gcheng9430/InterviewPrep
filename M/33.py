def solution(A, K):
    K = K-len(A)
    ans = K * (K + 1) // 2
    level = K + 1
    for x in sorted(set(A)):
        if x < level:
            ans += level - x
            level += 1
    return ans

def main():
    A = [6,5,4,1,3] 
    K = 7
    ans = solution(A, K)
    print(ans)

if __name__ == "__main__":
    main()