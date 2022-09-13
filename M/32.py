
def solution(nums):
    min_sum = 0
    max_sum = 0
    n = len(nums)

    stack = []
    for next_smaller in range(n+1):
        while stack and (next_smaller == n or nums[stack[-1]]>nums[next_smaller]):
            cur_smaller = stack.pop()
            if stack:
                last_smaller = stack[-1]
            else:
                last_smaller = -1
            min_sum += nums[cur_smaller]*(next_smaller - cur_smaller)*(cur_smaller - last_smaller)
        stack.append(next_smaller)
    
    # [4,-2,-3,4,1]
    # last index = -1
    # cur index = 0
    # next index = 1
    # min_sum += the frequency of a number that becomes the smallest in a subarray * the number

    stack = []
    for next_larger in range(n+1):
        while stack and (next_larger == n or nums[stack[-1]]<nums[next_larger]):
            cur_larger = stack.pop()
            if stack:
                last_larger = stack[-1]
            else:
                last_larger = -1
            max_sum += nums[cur_larger]*(next_larger - cur_larger)*(cur_larger - last_larger)
        stack.append(next_larger)

    return max_sum - min_sum

def main():
    input = [4,-2,-3,4,1]
    ans = solution(input)
    print(ans)

if __name__ == "__main__":
    main()