# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count/description/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain = defaultdict(int)
        
        for cpdomain in cpdomains:
            count, d = cpdomain.split(" ")
            count = int(count)
            
            subdomains = d.split(".")          
            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                domain[subdomain] += count

        ans = [str(count) + " " + subdomain for subdomain, count in domain.items()]
        
        return ans