from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        email_to_name = {}

        # init + union
        for acc in accounts:
            name = acc[0]
            first_email = acc[1]

            for email in acc[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(first_email, email)

        # group by root
        groups = defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)

        # build answer
        ans = []
        for root in groups:
            name = email_to_name[root]
            ans.append([name] + sorted(groups[root]))

        return ans