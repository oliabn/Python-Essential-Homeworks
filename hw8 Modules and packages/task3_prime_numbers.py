"""Task3
Створіть модуль для отримання простих чисел. Імпортуйте
його з іншого модуля. Імпортуйте його окремі імена.
"""


def prime_num(n: int):
    """Return n prime numbers"""

    def is_prime(num):
        """Check that number is prime"""
        if num < 2:
            return False
        for divisor in range(2, num):
            if num % divisor == 0:
                return False
        return True

    prime_numbers = []
    num = 2
    while len(prime_numbers) < n:
        if is_prime(num):
            prime_numbers.append(num)
        num += 1

    return prime_numbers


ten_prime_numbers = prime_num(10)
twenty_prime_numbers = prime_num(20)
