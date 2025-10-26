def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    # Check divisors from 3 to square root of num
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Find all prime numbers between start and end (inclusive)"""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Get input from user
try:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    
    if start > end:
        print("Start should be less than or equal to end!")
    else:
        primes = find_primes_in_range(start, end)
        print(f"\nPrime numbers between {start} and {end}:")
        print(primes)
        print(f"Total prime numbers found: {len(primes)}")
        
except ValueError:
    print("Please enter valid integers!")