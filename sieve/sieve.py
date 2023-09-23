def sieve_of_eratosthenes(limit):
    """Return a list of all prime numbers less than limit."""
    sieve = [True] * limit
    sieve[0:2] = [False, False]
    for current in range(2, int(limit**0.5) + 1):
        if sieve[current]:
            sieve[current*current:limit:current] = [False] * \
                len(sieve[current*current:limit:current])
    return [i for i, is_prime in enumerate(sieve) if is_prime]


if __name__ == "__main__":
    primes_up_to_100 = sieve_of_eratosthenes(101)
    print(primes_up_to_100)
