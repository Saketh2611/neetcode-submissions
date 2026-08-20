from typing import List

class Solution:
    def isdups(self, lists: List[str]) -> bool:
        visited = set()
        for strs in lists:
            if strs in visited:
                return True
            visited.add(strs)
        return False

    def removedups(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        ans.extend(list1)
        for stri in list2:
            if stri not in ans:
                ans.append(stri)
        return ans

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        groups = {}

        for acc in accounts:
            name = acc[0]
            emails = list(set(acc[1:]))

            if name not in groups:
                groups[name] = [emails]
            else:
                merged = False
                for i in range(len(groups[name])):
                    if set(groups[name][i]) & set(emails):
                        groups[name][i] = self.removedups(groups[name][i], emails)
                        merged = True
                        break
                if not merged:
                    groups[name].append(emails)

        # 🔁 transitive merge pass (important fix)
        for name in groups:
            changed = True
            while changed:
                changed = False
                new_lists = []
                used = [False]*len(groups[name])

                for i in range(len(groups[name])):
                    if used[i]:
                        continue
                    cur = groups[name][i]
                    for j in range(i+1, len(groups[name])):
                        if not used[j] and set(cur) & set(groups[name][j]):
                            cur = self.removedups(cur, groups[name][j])
                            used[j] = True
                            changed = True
                    new_lists.append(cur)
                groups[name] = new_lists

        ans = []
        for name in groups:
            for emails in groups[name]:
                ans.append([name] + sorted(emails))

        return ans