"""
Day 04 - Banking Project Milestone 1: Encapsulated Account Class
"""
from datetime import datetime

class Account:
    """
    Encapsulated Account class representing a bank account in ETB.
    """
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
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": tx_type,
            "amount": amount,
            "balance_after": self._balance
        })

    def get_balance(self) -> float:
        """Returns current balance."""
        return self._balance

    def deposit(self, amount: float) -> bool:
        """Deposits specified amount into account."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self._balance += amount
        self._record_transaction("DEPOSIT", amount)
        print(f"Successfully deposited ETB {amount:,.2f}. New Balance: ETB {self._balance:,.2f}")
        return True

    def withdraw(self, amount: float) -> bool:
        """Withdrew specified amount from account if sufficient funds exist."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self._balance:
            print(f"Insufficient funds! Requested: ETB {amount:,.2f}, Available: ETB {self._balance:,.2f}")
            return False
        self._balance -= amount
        self._record_transaction("WITHDRAWAL", amount)
        print(f"Successfully withdrew ETB {amount:,.2f}. Remaining Balance: ETB {self._balance:,.2f}")
        return True

    def get_statement(self) -> str:
        """Generates formatted bank statement."""
        lines = [
            f"=== Account Statement for {self.holder_name} ({self.account_number}) ===",
            f"Current Balance: ETB {self._balance:,.2f}",
            "--- Transaction History ---"
        ]
        for tx in self._transactions:
            lines.append(f"[{tx['timestamp']}] {tx['type']}: ETB {tx['amount']:,.2f} | Balance: ETB {tx['balance_after']:,.2f}")
        return "\n".join(lines)


if __name__ == "__main__":
    acc = Account("ETB-1001", "Aman Desalegn", 5000.0)
    acc.deposit(2500.0)
    acc.withdraw(1200.0)
    print("\n" + acc.get_statement())
