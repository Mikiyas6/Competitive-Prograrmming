class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        graph = defaultdict(list)
        email_to_name = {}
        
        # Build the graph connecting emails from the same account
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[account[1]].append(email)
                graph[email].append(account[1])  # Bidirectional connection
                email_to_name[email] = name

        visited = set()
        merged_accounts = []

        # Depth-first search to find connected components
        def dfs(email, component):
            if email not in visited:
                visited.add(email)
                component.append(email)
                for neighbor in graph[email]:
                    dfs(neighbor, component)

        # Iterate through each email and find connected components
        for email in email_to_name:
            if email not in visited:
                component = []
                dfs(email, component)
                merged_accounts.append([email_to_name[email]] + sorted(component))

        return merged_accounts
