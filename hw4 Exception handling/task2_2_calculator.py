"""Task2
Напишіть програму-калькулятор, яка підтримує такі операції: додавання,
віднімання, множення, ділення та піднесення до ступеня.
Програма має видавати повідомлення про помилку та продовжувати роботу під
час введення некоректних даних, діленні на нуль та зведенні нуля в негативний степінь.
"""

from task2_1_mathExpressionExecutor import MathExpressionExecutor


class Calculator(MathExpressionExecutor):
    _RED, _RESET = "\033[31m", "\033[0m"
    _BLUE, _YELLOW = "\033[36m", "\033[33m"
    _HELP = f"\n{_BLUE}Available operators: + - / * ^ ()\n" \
            f"E.g.: (9.3 + 1.7) * 2^2\n" \
            f"Enter <q> for exit{_RESET}"

    @classmethod
    def calculate(cls, expression: str) -> float:
        """Return the result of evaluating the expression."""

        expression = expression.replace('^', '**')
        return eval(expression)

    @classmethod
    def run(cls):
        while True:
            print(cls._HELP)
            expression = input("Enter expression: ")

            if expression == 'q':
                exit()

            if not cls._is_valid_expression(expression):
                print("Incorrect input. Try again")
                continue

            print(f"{cls._YELLOW}Result = {cls.calculate(expression)}{cls._RESET}")


if __name__ == '__main__':
    calc = Calculator()
    calc.run()
