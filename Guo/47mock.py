# few trip
# 1. choose 2 with same weight
# 2. choose 3 with same  weight

# min num of trips to deliver packages 
# not possible:-1

# int arr weight [2,4,6,6,4,2,4]
# 3 trips:
# 2 2  4 4 4  6 6 
# valToFreq:
# 2->1
# 4->3
# 6->2

# trips = 3

#intution: count the frequency of distince values, each time choose 3 per trip
#as much as we can, and cover the rest(if there is remainder) with one more trip
#runtime: O(n)
#space: O(n)

import collections
def minTrips(weight):
    valToFreq = collections.Counter(weight)
    trips =0
    for w,freq in valToFreq.items():
        #choose 3 per trip as much as possible
        trip,remain = divmod(freq,3)
        #if freq is divisible by 3, trip can deliver all, 
        # else need one more trip for the rest
        trips+= trip if remain ==0 else trip+1
    return trips



weight = [2,4,6,6,4,2,4]
print("Expted:3, Actual:",minTrips(weight))

