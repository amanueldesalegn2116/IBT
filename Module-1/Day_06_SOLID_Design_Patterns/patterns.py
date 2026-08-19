"""
Day 06 - SOLID Principles & Design Patterns Implementation
"""
import threading

# 1. SINGLETON PATTERN: BankLogger
class BankLogger:
    """Thread-safe Singleton Logger."""
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._logs = []
            return cls._instance

    def log(self, message: str):
        self._logs.append(message)
        print(f"[LOGGER] {message}")

    def get_logs(self) -> list:
        return list(self._logs)


# 2. OBSERVER PATTERN: Transaction Notification
class Observer:
    def update(self, account_number: str, event_type: str, amount: float):
        pass


class AuditLogObserver(Observer):
    def update(self, account_number: str, event_type: str, amount: float):
        logger = BankLogger()
        logger.log(f"AuditLog: Account {account_number} executed {event_type} of ETB {amount:,.2f}")


class SMSNotificationObserver(Observer):
    def update(self, account_number: str, event_type: str, amount: float):
        print(f"[SMS ALERT] Account {account_number}: {event_type} ETB {amount:,.2f} processed.")


class ObservableAccount:
    def __init__(self, account_number: str, holder_name: str, balance: float = 0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self._balance = balance
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def notify(self, event_type: str, amount: float):
        for obs in self._observers:
            obs.update(self.account_number, event_type, amount)

    def deposit(self, amount: float):
        self._balance += amount
        self.notify("DEPOSIT", amount)


# 3. FACTORY PATTERN: AccountFactory
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class AccountFactory:
    """Factory for creating accounts based on type."""
    @staticmethod
    def create_account(account_type: str, account_number: str, holder_name: str, balance: float = 0.0):
        acc_type_lower = account_type.lower()
        if acc_type_lower in ["savings", "sav"]:
            from Day_05_OOP_Inheritance.bank import SavingsAccount
            return SavingsAccount(account_number, holder_name, balance)
        elif acc_type_lower in ["current", "cur"]:
            from Day_05_OOP_Inheritance.bank import CurrentAccount
            return CurrentAccount(account_number, holder_name, balance)
        else:
            raise ValueError(f"Unknown account type: {account_type}")


if __name__ == "__main__":
    logger1 = BankLogger()
    logger2 = BankLogger()
    print("Singleton Verified (logger1 is logger2):", logger1 is logger2)

    acc = ObservableAccount("OBS-001", "Taye Atske", 10000.0)
    acc.attach(AuditLogObserver())
    acc.attach(SMSNotificationObserver())
    acc.deposit(5000.0)
