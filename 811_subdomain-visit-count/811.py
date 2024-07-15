#
# @lc app=leetcode id=811 lang=python3
#
# [811] Subdomain Visit Count
#
from typing import *
# @lc code=start
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d={}
        for i in cpdomains:
            rep, url = tuple(i.split(" "))
            rep = int(rep)
            domains = url.split('.')
            for j in range(len(domains)):
                subdomain = '.'.join(domains[j:])
                if subdomain in d:
                    d[subdomain]+=rep
                else:
                    d[subdomain] = rep
        res=[]
        for i in d:
            res.append("{ct} {domain}".format(ct=d[i], domain=i))
        return res
# @lc code=end

