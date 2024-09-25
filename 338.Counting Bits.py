class Solution:
    def countBits(self, num: int) -> List[int]:
        results = [0]
        
        for i in range(1, num+1):
            results.append(results[i & (i-1)] + 1)
            
        return results