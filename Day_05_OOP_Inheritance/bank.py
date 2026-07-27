"""
Day 05 - Banking Project Milestone 2: Savings & Current Accounts
"""
import sys
import os

# Import base Account class from Day 4 if needed, or define integrated hierarchy
class Account:
    def __init__(self, account_number: str, holder_name: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_number = account_number
        self.holder_name = holder_name
        self._balance = float(initial_balance)
        self._transactions = []
        if initial_balance > 0:
            self._record_transaction("INITIAL DEPOSIT", initial_balance)

    def _record_transaction(self, tx_type: str, amount: float):
        self._transactions.append({
            "type": tx_type,
            "amount": amount,
            "balance_after": self._balance
        })

    def get_balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self._balance += amount
        self._record_transaction("DEPOSIT", amount)
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self._balance:
            print("Insufficient funds.")
            return False
        self._balance -= amount
        self._record_transaction("WITHDRAWAL", amount)
        return True


class SavingsAccount(Account):
    """
    Savings Account with interest rate and minimum balance enforcement.
    """
    def __init__(self, account_number: str, holder_name: str, initial_balance: float = 0.0,
                 interest_rate: float = 0.07, min_balance: float = 500.0):
        super().__init__(account_number, holder_name, initial_balance)
        self.interest_rate = interest_rate
        self.min_balance = min_balance

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if (self._balance - amount) < self.min_balance:
            print(f"Transaction Rejected! Cannot breach minimum balance of ETB {self.min_balance:,.2f}")
            return False
        self._balance -= amount
        self._record_transaction("WITHDRAWAL", amount)
        return True

    def apply_interest(self) -> float:
        """Applies annual interest to the account."""
        interest = self._balance * self.interest_rate
        self._balance += interest
        self._record_transaction("INTEREST APPLIED", interest)
        print(f"Applied ETB {interest:,.2f} interest. New Balance: ETB {self._balance:,.2f}")
        return interest


class CurrentAccount(Account):
    """
    Current Account with overdraft facility.
    """
    def __init__(self, account_number: str, holder_name: str, initial_balance: float = 0.0,
                 overdraft_limit: float = 5000.0):
        super().__init__(account_number, holder_name, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        available = self._balance + self.overdraft_limit
        if amount > available:
            print(f"Transaction Rejected! Overdraft limit of ETB {self.overdraft_limit:,.2f} exceeded.")
            return False
        self._balance -= amount
        self._record_transaction("WITHDRAWAL (OVERDRAFT OK)", amount)
        print(f"Withdrew ETB {amount:,.2f}. Current Balance: ETB {self._balance:,.2f}")
        return True


if __name__ == "__main__":
    savings = SavingsAccount("SAV-101", "Kassahun Tadesse", 2000.0, interest_rate=0.07, min_balance=500.0)
    savings.apply_interest()
    savings.withdraw(1800.0)  # Should reject (breaches min_balance)

    current = CurrentAccount("CUR-202", "Mesfin Haile", 1000.0, overdraft_limit=3000.0)
    current.withdraw(2500.0)  # Should succeed using overdraft
