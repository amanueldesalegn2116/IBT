"""
Day 03 - Practice Exercises
"""
import csv
import io
import re

def count_word_frequency(text: str) -> dict:
    """Exercise 1: Returns frequency dictionary of words in text."""
    words = re.findall(r'\b\w+\b', text.lower())
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def parse_customer_csv(csv_content: str) -> list:
    """Exercise 2: Parses CSV string into list of customer dicts."""
    customers = []
    reader = csv.DictReader(io.StringIO(csv_content.strip()))
    for row in reader:
        customers.append({
            "id": int(row["id"]),
            "name": row["name"],
            "balance": float(row["balance"]),
            "city": row["city"]
        })
    return customers

def safe_read_file(filepath: str) -> str:
    """Exercise 3: Safely reads a file with exception handling."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File '{filepath}' not found."
    except PermissionError:
        return f"Error: Permission denied for file '{filepath}'."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def analyze_log_summary(log_lines: list) -> dict:
    """Exercise 4: Analyzes log lines and returns level counts."""
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    errors = []
    for line in log_lines:
        for level in counts:
            if level in line:
                counts[level] += 1
                if level == "ERROR":
                    errors.append(line)
    return {"counts": counts, "error_logs": errors}

def process_transaction_batch(initial_balance: float, transactions: list) -> tuple:
    """Exercise 5: Processes transaction list and returns (final_balance, status_log)."""
    current = initial_balance
    log = []
    for tx in transactions:
        tx_type = tx.get("type")
        amount = tx.get("amount", 0.0)
        if tx_type == "deposit":
            current += amount
            log.append(f"Deposited ETB {amount:,.2f}. New Balance: ETB {current:,.2f}")
        elif tx_type == "withdrawal":
            if current < amount:
                log.append(f"REJECTED Withdrawal of ETB {amount:,.2f}: Insufficient Funds.")
            else:
                current -= amount
                log.append(f"Withdrew ETB {amount:,.2f}. New Balance: ETB {current:,.2f}")
    return current, log

if __name__ == "__main__":
    text = "Hello world! Hello Python programming world."
    print("Word Freq:", count_word_frequency(text))
    
    csv_sample = "id,name,balance,city\n1,Abebe,5000.0,Addis Ababa\n2,Kebede,3500.5,Hawassa"
    print("Parsed CSV:", parse_customer_csv(csv_sample))
    
    logs = ["INFO: System started", "WARNING: Disk 80% full", "ERROR: Connection failed"]
    print("Log Analysis:", analyze_log_summary(logs))
