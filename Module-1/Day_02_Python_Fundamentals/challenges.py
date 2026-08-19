"""
Day 02 - Coding Challenges (from m01-coding-questions.pdf)
"""

def fizz_buzz(n: int) -> list:
    """Challenge 1: Returns FizzBuzz list up to n."""
    res = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res

def is_prime(n: int) -> bool:
    """Challenge 2: Checks if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start: int, end: int) -> list:
    """Returns all prime numbers in range [start, end]."""
    return [num for num in range(start, end + 1) if is_prime(num)]

def is_palindrome(val) -> bool:
    """Challenge 3: Checks if string or integer is a palindrome."""
    s = str(val).lower()
    cleaned = ''.join(c for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    print("FizzBuzz(15):", fizz_buzz(15))
    print("Is 17 prime?:", is_prime(17))
    print("Primes 10-30:", primes_in_range(10, 30))
    print("Is 'racecar' palindrome?:", is_palindrome("racecar"))
    print("Is 12321 palindrome?:", is_palindrome(12321))
