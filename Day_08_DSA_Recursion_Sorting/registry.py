"""
Day 08 - Banking Project Milestone 4: Searchable & Rankable Account Registry
"""

class SearchableAccountRegistry:
    """
    Registry with O(log n) Binary Search and QuickSort Ranking by Balance.
    """
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        # Keep accounts sorted by account_number for binary search
        self.accounts.sort(key=lambda acc: acc.account_number)

    def search_by_account_number(self, account_number: str):
        """Binary Search for account by account_number."""
        low = 0
        high = len(self.accounts) - 1
        while low <= high:
            mid = (low + high) // 2
            curr_acc = self.accounts[mid]
            if curr_acc.account_number == account_number:
                return curr_acc
            elif curr_acc.account_number < account_number:
                low = mid + 1
            else:
                high = mid - 1
        return None

    def rank_accounts_by_balance(self, descending: bool = True) -> list:
        """Returns accounts sorted by balance using QuickSort concept."""
        def _quicksort(acc_list):
            if len(acc_list) <= 1:
                return acc_list
            pivot = acc_list[len(acc_list) // 2].get_balance()
            left = [a for a in acc_list if a.get_balance() > pivot] if descending else [a for a in acc_list if a.get_balance() < pivot]
            middle = [a for a in acc_list if a.get_balance() == pivot]
            right = [a for a in acc_list if a.get_balance() < pivot] if descending else [a for a in acc_list if a.get_balance() > pivot]
            return _quicksort(left) + middle + _quicksort(right)

        return _quicksort(list(self.accounts))


if __name__ == "__main__":
    import sys, os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    from Day_04_OOP_Encapsulation.account import Account

    reg = SearchableAccountRegistry()
    reg.add_account(Account("ETB-103", "Sifan Hassan", 75000.0))
    reg.add_account(Account("ETB-101", "Derartu Tulu", 45000.0))
    reg.add_account(Account("ETB-102", "Kenenisa Bekele", 90000.0))

    found = reg.search_by_account_number("ETB-102")
    if found:
        print("Binary Search Found:", found.holder_name, "Balance: ETB", found.get_balance())

    print("\n--- Accounts Ranked by Balance (High to Low) ---")
    ranked = reg.rank_accounts_by_balance()
    for acc in ranked:
        print(f"{acc.holder_name} ({acc.account_number}): ETB {acc.get_balance():,.2f}")
