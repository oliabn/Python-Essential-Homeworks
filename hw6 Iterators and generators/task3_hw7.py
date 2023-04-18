"""task3 hw7
Напишіть функцію-генератор для отримання n перших простих чисел
"""


def prime_num(n: int):

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
    while n:
        if is_prime(num):
            n -= 1
            prime_numbers.append(num)
            yield num
        num += 1


if __name__ == '__main__':
    for num in prime_num(5):
        print(num)
