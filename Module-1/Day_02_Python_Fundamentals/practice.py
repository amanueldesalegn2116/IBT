"""
Day 02 - Practice Exercises
"""

def format_welcome_message(name: str, balance: float) -> str:
    """Exercise 1: Returns formatted welcome message with ETB currency formatting."""
    return f"Welcome, {name}! Your initial balance is ETB {balance:,.2f}."

def calculate_age_and_leap_year(birth_year: int, current_year: int = 2026) -> dict:
    """Exercise 2: Calculates age in years, estimated days, and checks leap year."""
    age_years = current_year - birth_year
    age_days = int(age_years * 365.25)
    is_leap = (birth_year % 4 == 0 and birth_year % 100 != 0) or (birth_year % 400 == 0)
    return {
        "age_years": age_years,
        "age_days": age_days,
        "is_leap_year": is_leap
    }

def get_letter_grade(score: float) -> str:
    """Exercise 3: Returns letter grade for score between 0 and 100."""
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def convert_temperature(value: float, unit: str) -> float:
    """Exercise 4: Converts temperature between 'C' and 'F'."""
    unit_upper = unit.upper()
    if unit_upper == 'C':
        return (value * 9 / 5) + 32  # to Fahrenheit
    elif unit_upper == 'F':
        return (value - 32) * 5 / 9  # to Celsius
    else:
        raise ValueError("Unit must be 'C' or 'F'")

def calculate(a: float, b: float, operator: str) -> float:
    """Exercise 5: CLI Calculator operation."""
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    elif operator == '%':
        if b == 0:
            raise ZeroDivisionError("Cannot modulo by zero.")
        return a % b
    else:
        raise ValueError(f"Unsupported operator: {operator}")

if __name__ == "__main__":
    print(format_welcome_message("Abebe", 15000.5))
    print("Age info:", calculate_age_and_leap_year(2000))
    print("Grade for 85:", get_letter_grade(85))
    print("25C in F:", convert_temperature(25, 'C'))
    print("10 / 2 =", calculate(10, 2, '/'))
