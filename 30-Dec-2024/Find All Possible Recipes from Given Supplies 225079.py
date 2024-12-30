# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        graph = defaultdict(list)
        outgoing = defaultdict(int)

        for i in range(len(recipes)):
            for ing in ingredients[i]:
                graph[ing].append(recipes[i])
                outgoing[recipes[i]] += 1

        res = set()
        queue = deque([i for i in supplies if not outgoing[i]])
  
        while queue:
            node = queue.popleft()
            res.add(node)
            for nd in graph[node]:
                outgoing[nd] -= 1
                if not outgoing[nd]:
                    queue.append(nd)
        

        return [recipe for recipe in recipes if recipe in res]