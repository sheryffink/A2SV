class Solution:    
    def findUnion(self, a, b):
        setA = set(a)
        setB = set(b)
        union = setA | setB
        number_of_elements = len(union)
        
        return number_of_elements
