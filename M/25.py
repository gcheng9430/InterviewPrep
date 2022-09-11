def solution(nums):
    if len(nums) == 2:
        return nums
    cur = []
    for i in range(len(nums)-1):
        cur.append((nums[i]+nums[i+1])%10)
    return solution(cur)

def main():
    numbers = [4, 5, 6, 7] 
    ans = solution(numbers)
    print(ans)

if __name__ == "__main__":
    main()