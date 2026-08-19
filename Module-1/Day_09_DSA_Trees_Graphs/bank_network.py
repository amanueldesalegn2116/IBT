"""
Day 09 - Banking Project Milestone 5: Bank Hierarchy Tree & Money Transfer Graph
"""
from collections import deque

class BranchNode:
    """Tree node representing a Bank Branch."""
    def __init__(self, name: str, total_deposits: float = 0.0):
        self.name = name
        self.total_deposits = total_deposits
        self.children = []

    def add_sub_branch(self, child_node):
        self.children.append(child_node)

    def calculate_subtree_deposits(self) -> float:
        """Calculates total deposits of branch and all sub-branches."""
        total = self.total_deposits
        for child in self.children:
            total += child.calculate_subtree_deposits()
        return total


class TransferNetwork:
    """Directed Graph representing inter-account money transfer flow."""
    def __init__(self):
        self.graph = {}

    def record_transfer(self, sender: str, receiver: str, amount: float):
        self.graph.setdefault(sender, []).append({"receiver": receiver, "amount": amount})
        self.graph.setdefault(receiver, [])

    def trace_transfer_paths(self, start_account: str) -> list:
        """BFS trace of transfer paths starting from an account."""
        visited = set([start_account])
        queue = deque([start_account])
        path = []
        while queue:
            curr = queue.popleft()
            path.append(curr)
            for tx in self.graph.get(curr, []):
                nxt = tx["receiver"]
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
        return path


if __name__ == "__main__":
    # Branch Hierarchy Tree
    hq = BranchNode("CBE Head Office", 10000000.0)
    addis_hub = BranchNode("Addis Ababa Regional Office", 5000000.0)
    oromia_hub = BranchNode("Oromia Regional Office", 3000000.0)
    hq.add_sub_branch(addis_hub)
    hq.add_sub_branch(oromia_hub)

    addis_hub.add_sub_branch(BranchNode("Bole Branch", 1500000.0))
    addis_hub.add_sub_branch(BranchNode("Piassa Branch", 1200000.0))

    print(f"Total Bank System Deposits across Subtree: ETB {hq.calculate_subtree_deposits():,.2f}")

    # Transfer Network Graph
    network = TransferNetwork()
    network.record_transfer("ETB-101", "ETB-102", 5000.0)
    network.record_transfer("ETB-102", "ETB-103", 2000.0)
    network.record_transfer("ETB-103", "ETB-104", 1500.0)
    print("Transfer Path from ETB-101:", network.trace_transfer_paths("ETB-101"))
