def solution(awards, k):
    left = right = 0
    awards.sort()
    ans = 0
    while right < len(awards):
        if awards[right] - awards[left] > k:
            ans += 1
            left = right
        right += 1
    return ans+1

def main():
    A = [1,5,4,6,8,9,2] 
    K = 3
    ans = solution(A, K)
    print(ans)

if __name__ == "__main__":
    main()