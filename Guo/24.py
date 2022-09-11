import heapq
def getSmallestInefficiencies(skill,k):
    #intuition: sort the skill array, put each consecutive pair and their difference
    #into a priority q, while result array of length k is not filled, get the smallest
    #difference pair from the pq and push (i,j+1) (we don't also do (i-1,j) just to avoid 
    # repetition )
    #runtime: O(nlog for sort, (n+k)logn for pq)=O((n+k)logN) if k goes up to n^2 then n^2logn
    #space: O(logn for sort and n for pq)=O(n)

    skill.sort()
    q = []
    #push each consecutive pair into the priority queue
    for i in range(len(skill)-1):
        heapq.heappush(q,(skill[i+1]-skill[i],i,i+1)) #diff,firstIdx,secondIdx
    
    res = [] #k least pair differences in ascending order
    while len(res)<k:
        #get the smallest difference
        diff,first,second = heapq.heappop(q)
        res.append(diff)
        #change second index to one larger and push into pq
        if second<len(skill)-1:
            heapq.heappush(q,(skill[second+1]-skill[first],first,second+1))
    return res


#test
skill = [6,9,1]
k=2
print("Expted:[3,5], Actual:",getSmallestInefficiencies(skill,k))
