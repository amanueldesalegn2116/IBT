"""
Day 06 — Refactored Bank System
Patterns applied:
  • SRP        – AlertService is split out of Account
  • Factory    – AccountFactory.create() builds accounts by type
  • Observer   – subscribe() / _notify() + SMSAlert / AuditLog observers
  • Singleton  – BankConfig holds shared settings (interest rate, overdraft limit)
"""

# ──────────────────────────────────────────────
# 1. Singleton — BankConfig (one shared config)
# ──────────────────────────────────────────────
class BankConfig:
    """Single source of truth for bank-wide settings."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000
        return cls._instance


# ──────────────────────────────────────────────
# 2. Observer — Alert classes (SRP: separated from Account)
# ──────────────────────────────────────────────
class SMSAlert:
    """TeleBirr SMS notification observer."""
    def update(self, event):
        print(f"[TeleBirr SMS] {event}")


class AuditLog:
    """Audit trail observer."""
    def update(self, event):
        print(f"[Log] {event}")


# ──────────────────────────────────────────────
# 3. Account family (with Observer support)
# ──────────────────────────────────────────────
class Account:
    """Base account with observer (subscribe / _notify) support."""

    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self.balance = balance
        self._observers = []           # Observer list

    # ---- Observer plumbing ----
    def subscribe(self, observer):
        """Attach an observer that will be notified of account events."""
        self._observers.append(observer)

    def _notify(self, event):
        """Push an event string to every subscribed observer."""
        for obs in self._observers:
            obs.update(event)

    # ---- Banking operations ----
    def deposit(self, amount):
        self.balance += amount
        self._notify(f"+{amount} ETB on {self.number}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self._notify(f"-{amount} ETB on {self.number}")

    def statement(self):
        print(f"{self.owner}: {self.balance} ETB")


class SavingsAccount(Account):
    """Savings account — earns interest from BankConfig."""

    def apply_interest(self):
        rate = BankConfig().interest_rate
        interest = self.balance * rate
        self.balance += interest
        self._notify(f"+{interest:.2f} ETB interest on {self.number}")

    def statement(self):
        print(f"[Savings] {self.owner} ({self.number}): {self.balance:.2f} ETB")


class CurrentAccount(Account):
    """Current account — allows overdraft up to BankConfig limit."""

    def withdraw(self, amount):
        limit = BankConfig().overdraft_limit
        if amount > self.balance + limit:
            print("Exceeds overdraft limit.")
            return
        self.balance -= amount
        self._notify(f"-{amount} ETB on {self.number}")

    def statement(self):
        print(f"[Current] {self.owner} ({self.number}): {self.balance:.2f} ETB")


# ──────────────────────────────────────────────
# 4. Factory — AccountFactory.create()
# ──────────────────────────────────────────────
class AccountFactory:
    """Centralises object creation — the rest of the code never names a class."""

    @staticmethod
    def create(kind, owner, number, balance=0):
        if kind == "savings":
            return SavingsAccount(owner, number, balance)
        if kind == "current":
            return CurrentAccount(owner, number, balance)
        raise ValueError(f"Unknown account type: {kind}")


# ──────────────────────────────────────────────
# 5. Demo — wire everything together
# ──────────────────────────────────────────────
if __name__ == "__main__":

    # --- Singleton demo ---
    config = BankConfig()
    print(f"Interest rate : {config.interest_rate}")
    print(f"Overdraft cap : {config.overdraft_limit}")
    print()

    # --- Factory creates accounts ---
    acc1 = AccountFactory.create("savings", "Almaz", "CBE-1", 1500)
    acc2 = AccountFactory.create("current", "Dawit", "CBE-2", 3000)

    # --- Attach observers (Observer pattern) ---
    sms = SMSAlert()
    log = AuditLog()

    acc1.subscribe(sms)
    acc1.subscribe(log)
    acc2.subscribe(sms)
    acc2.subscribe(log)

    # --- Perform operations ---
    print("— Savings account —")
    acc1.deposit(500)
    acc1.apply_interest()
    acc1.statement()
    print()

    print("— Current account —")
    acc2.withdraw(5000)
    acc2.statement()
    print()

    # --- Prove singleton identity ---
    a = BankConfig()
    b = BankConfig()
    print(f"Same BankConfig? {a is b}")   # True
