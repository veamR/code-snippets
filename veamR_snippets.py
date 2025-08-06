# veamR's Favorite Python Snippets

def fibonacci(n):
    """Return the nth Fibonacci number."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def factorial(n):
    """Return the factorial of n."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def reverse_string(s):
    """Return the reversed version of a string."""
    return s[::-1]
