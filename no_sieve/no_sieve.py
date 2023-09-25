def is_prime(n):
    """Return True if n is a prime number, else False."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    limit = int(input("いくつまでの素数を出力しますか？: "))
    import time
    start_time = time.time()
    primes = [i for i in range(2, limit+1) if is_prime(i)]
    end_time = time.time()
    print(primes)
    print(f"計算時間: {end_time - start_time:.5f}秒")
