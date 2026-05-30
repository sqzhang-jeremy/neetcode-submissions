class DSU:
    def __init__(self, n):
        self.comps = n
        self.Parent = list(range(n + 1)) # create a parent list from 0 to n
        self.rank = [1] * (n + 1) # create each height from 0 to n with 1
    
    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]
    
    def union(self, u, v):
        pu = self.find(u) 
        pv = self.find(v)

        if pu == pv:
            return False #cycle
        
        self.comps -= 1

        if self.rank[pu] < self.rank[pv]: #ensure pu is the root of the bigger tree
            pu, pv = pv, pu
        
        self.rank[pu] += self.rank[pv]
        self.Parent[pv] = pu
        
        return True

    def components(self):
        return self.comps



class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > n -1:
            return False
        
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        
        return dsu.components() == 1
        