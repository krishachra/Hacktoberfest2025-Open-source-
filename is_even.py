def is_even(n):
    """
    Returns True if the number is even, False otherwise.
    """
    return n % 2 == 0

# User input
num = int(input("Enter a number: "))
if is_even(num):
    print("The number is even.")
else:
    print("The number is odd.")

# Test cases
assert is_even(2) == True
assert is_even(7) == False
assert is_even(0) == True
