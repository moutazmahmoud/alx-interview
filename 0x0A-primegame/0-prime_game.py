#!/usr/bin/python3
"""
Prime Game module
Maria and Ben play a game using consecutive integers. The winner is determined
by their ability to pick primes optimally.
"""


def sieve_of_eratosthenes(n):
    """Returns a list of prime numbers up t
    o n using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False

    return [num for num, prime in enumerate(is_prime) if prime]


def isWinner(x, nums):
    """
    Determines the winner of the prime game.
    :param x: number of rounds
    :param nums: list of n values for each round
    :return: Winner name ("Maria", "Ben", or None)
    """
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Precompute win counts for Maria
    maria_wins = [0] * (max_n + 1)
    for num in range(1, max_n + 1):
        turn_count = 0
        remaining_numbers = list(range(1, num + 1))
        used = set()

        for prime in primes:
            if prime > num:
                break
            if prime not in used:
                turn_count += 1
                # Remove prime and its multiples
                for multiple in range(prime, num + 1, prime):
                    used.add(multiple)

        maria_wins[num] = 1 if turn_count % 2 != 0 else -1

    # Determine winner for each round
    maria_score = 0
    ben_score = 0

    for n in nums:
        if maria_wins[n] == 1:
            maria_score += 1
        elif maria_wins[n] == -1:
            ben_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    return None
