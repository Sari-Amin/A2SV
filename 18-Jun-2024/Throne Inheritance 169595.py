# Problem: Throne Inheritance - https://leetcode.com/problems/throne-inheritance/

class ThroneInheritance:
    def __init__(self, kingName):
        self.kingName = kingName
        self.dict1 = defaultdict(list)
        self.ans = set()
        
    def birth(self, parentName, childName):
        self.dict1[parentName].append(childName)

    def death(self, name):
        self.ans.add(name)

    def getInheritanceOrder(self):
        def dfs(node):
            if not node:
                return 

            res = [node]

            for neighbor in self.dict1[node]:
                res += dfs(neighbor)

            return res 

        result = dfs(self.kingName)

        return [i for i in result if i not in self.ans]
        

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()