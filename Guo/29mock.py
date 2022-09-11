# input: string searchWord, resultWord
# armaze

# armaze o
# armaze on

# amazon 
# ptr=4  6 2
#runtime: O(n)
#space: O(1)
def solution(searchWord,resultWord):
    m = len(searchWord)
    n = len(resultWord)
    ptr = 0
    #iterate search Word and match as many char in resultWord as Possible
    for i in range(m):
        #has matched all of resultWord, no need to add
        if ptr ==n:
            return 0
        if searchWord[i]==resultWord[ptr]:
            ptr +=1
    #add rest of  resultWord
    return n-ptr

searchWord =  "armaze"
resultWord  = "amazon"
print("Expted:2, Actual:",solution(searchWord,resultWord))


