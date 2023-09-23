def is_prime(n):
    """Return True if n is a prime number, else False."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    primes_up_to_100 = [i for i in range(2, 101) if is_prime(i)]
    print(primes_up_to_100)
