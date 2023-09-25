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
    limit = int(input("いくつまでの素数を出力しますか？: "))
    import time
    start_time = time.time()
    primes = sieve_of_eratosthenes(limit+1)
    end_time = time.time()
    print(primes)
    print(f"計算時間: {end_time - start_time:.5f}秒")
