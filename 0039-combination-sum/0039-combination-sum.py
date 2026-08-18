class Solution:
    def combinationSum(self, candidates, target):

        result = [] # store no. 

        def backtrack(index, current_list, total): #current position ,helping func.

            if total == target:
                result.append(current_list.copy()) #save ans
                return

            if total > target:
                return #pruning bykar rasta band krna, dead end

            for i in range(index, len(candidates)): # 1st sy last

                current_list.append(candidates[i]) #select no.

                backtrack(i, current_list, total + candidates[i]) 

                current_list.pop() #current position

        backtrack(0, [], 0) #start recursion

        return result