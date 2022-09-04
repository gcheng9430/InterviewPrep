# input: array processPower[] , bootingPower[], int maxPower
# choose longest consecutive subarray, sum of consumption < maxPower
# sum of consumption: max(booting)+sum(process)*k < maxPow

# max = 5
# sum of processing power=2+1+3=6
# max pooting power=6
# power consumption=6+6*3=24<25

# 2,1,3,4,5 process
# 6,6,6,3,4 booting
# maxPower = 25
# left =0
# right = 3
# n = 0
# sum = 8
# [6,6,6,3]   6+10*4=<25
# maxLen = 3

#intuition: monoQueue to keep track of max booting power in window
            #variable sum to keep track of sum of process power in window
            #left and right pointer to keep track of length
#O(n) and O(n)
import collections
def solution(processPower,bootingPower,maxPower):
    n = len(processPower)
    monoQ = collections.deque() #nonincreasing 
    left = 0
    right = 0
    windowSum = 0
    maxLen = 0
    while right<n:
        #extend window by 1
        currProcess = processPower[right]
        currBooting = bootingPower[right]
        windowSum+=currProcess
        while monoQ and monoQ[-1]<currBooting:
            monoQ.pop()
        monoQ.append(currBooting)
        #shrink window until requirement met

        while monoQ and monoQ[0]+windowSum*(right-left+1)>maxPower:
            leftProcess = processPower[left]
            leftBooting = bootingPower[left]
            windowSum -= leftProcess
            left+=1
            if monoQ and monoQ[0]==leftBooting:
                monoQ.popleft()
        #update length
        maxLen = max(maxLen,right-left+1)
        right +=1

    return maxLen

processPower=[2,1,3,4,5] 
bootingPower = [6,6,6,3,4] 
maxPower = 25
print("Expected:3, Actual: ",solution(processPower,bootingPower,maxPower))