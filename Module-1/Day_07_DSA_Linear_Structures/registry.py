"""
Day 07 - Banking Project Milestone 3: Account Registry
"""

class AccountNode:
    def __init__(self, account):
        self.account = account
        self.next = None


class AccountRegistry:
    """
    Account Registry using custom linked list structure to manage accounts.
    """
    def __init__(self):
        self.head = None
        self._count = 0

    def add_account(self, account):
        """Adds account to registry."""
        new_node = AccountNode(account)
        new_node.next = self.head
        self.head = new_node
        self._count += 1
        print(f"Registered account {account.account_number} for {account.holder_name}.")

    def find_by_number(self, account_number: str):
        """Finds account by account number."""
        curr = self.head
        while curr:
            if curr.account.account_number == account_number:
                return curr.account
            curr = curr.next
        return None

    def get_total_system_balance(self) -> float:
        """Calculates sum of balances across all registered accounts."""
        total = 0.0
        curr = self.head
        while curr:
            total += curr.account.get_balance()
            curr = curr.next
        return total

    def list_all(self) -> list:
        accounts = []
        curr = self.head
        while curr:
            accounts.append(curr.account)
            curr = curr.next
        return accounts


if __name__ == "__main__":
    import sys, os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    from Day_04_OOP_Encapsulation.account import Account

    registry = AccountRegistry()
    registry.add_account(Account("ETB-101", "Almaz Ayana", 12000.0))
    registry.add_account(Account("ETB-102", "Haile Gebrselassie", 50000.0))

    acc = registry.find_by_number("ETB-101")
    if acc:
        print("Found:", acc.holder_name, "Balance:", acc.get_balance())

    print("Total System Balance: ETB", registry.get_total_system_balance())
