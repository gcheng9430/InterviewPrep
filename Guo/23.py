class Solution:

    #intution: if max is larger or equal to armor, all armor can be used up,
    #else only use armor on the max damage. Add 1 to result because health  has to remian larger than 0
    #runtime: O(n)
    #space: O(1)
    def minimumHealth(self, damage, armor) -> int:
        total = sum(damage)
        maxNum = max(damage)
        #if max is larger or equal to armor, all armor can be used up
        if maxNum >=  armor:
            return total+1-armor
        else: #else only use armor on the max damage
            return total+1-maxNum

a  = Solution()
damage = [2,7,4,3]
armor = 4
print("Expted:13, Actual:",a.minimumHealth(damage,armor))