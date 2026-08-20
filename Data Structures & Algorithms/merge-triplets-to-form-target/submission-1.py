class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        trip = 0
        visits = [False] * 3
        for u,v,w in triplets:
            if u <= target[0] and v <= target[1] and w <= target[2] :
                if trip == 3 : 
                    return True 
                    break
                if u == target[0] and not visits[0] :
                    trip += 1 
                    visits[0] = True
                if v == target[1] and not visits[1]:
                    trip += 1 
                    visits[1] = True 
                if w == target[2] and not visits[2] :
                    trip += 1
                    visits[2] = True
        if trip == 3 : 
            return True
        else : 
            return False
                


        