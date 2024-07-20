# https://www.geeksforgeeks.org/problems/check-if-two-strings-are-k-anagrams-or-not/1


class Solution:
    def areKAnagrams(self, str1, str2, k):
        # code here
        if len(str1) != len(str2):
            return False
            
        count1 = [0] * 26
        count2 = [0] * 26
        changes = 0
        
        for i in range(0,len(str1)):
            count1[ord(str1[i]) - 97] += 1
            count2[ord(str2[i]) - 97] += 1
            
        for i in range(0, len(count1)):
            if count1[i] > count2[i]:
                changes += (count1[i] - count2[i])
                
            if changes > k:
                return False
                
        return True