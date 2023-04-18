"""Task2
Напишіть програму-калькулятор, яка підтримує такі операції: додавання,
віднімання, множення, ділення та піднесення до ступеня.
Програма має видавати повідомлення про помилку та продовжувати роботу під
час введення некоректних даних, діленні на нуль та зведенні нуля в негативний степінь.
"""


class MathExpressionExecutor:
    """Calculates mathematical expressions with operations +, -, /, *, ^-power.
    Gets a str with a mathematical expression, returns the result of the calculation"""

    _AVAILABLE_OP = ['+', '-', '/', '*', '^', '(', ')', '.', 'q']
    _RED, _RESET = "\033[31m", "\033[0m"

    @classmethod
    def _is_valid_expression(cls, expression: str) -> bool:
        """Check that the user's expression is valid for that calculator"""

        def is_valid_op(op):
            return op in cls._AVAILABLE_OP

        def is_number(val):
            try:
                float(val)
                return True
            except ValueError:
                return False

        for elem in cls._split_up_operators_numbers(expression):
            if not is_valid_op(elem) and not is_number(elem):
                print(f'{cls._RED}SyntaxError: Use only available operators: + - / * ^ () and numbers{cls._RESET}')
                return False

        expression = expression.replace('^', '**')
        try:
            eval(expression)
            return True
        except (SyntaxError, NameError):
            print(f"{cls._RED}SyntaxError: Math expression isn't correct.{cls._RESET}")
            return False
        except ZeroDivisionError as error:
            print(f"{cls._RED}{error}{cls._RESET}")
            return False
        except Exception as error:
            print(f"{cls._RED}{error}{cls._RESET}")
            return False

    @staticmethod
    def _split_up_operators_numbers(expression) -> list:
        """Split up the expression into operators and numbers.
        E.g. '3.9*4.8 - 6+99.99' -> ['3.9', '*', '4.8', '-', '6', '+', '99.99']"""

        operators_and_num = expression[0]

        for prev_char, next_char in zip(expression, expression[1:]):
            if ((prev_char.isdigit() or prev_char == '.')
                    and (next_char.isdigit() or next_char == '.')):
                operators_and_num += next_char
            else:
                operators_and_num += " " + next_char

        return operators_and_num.split()

    @classmethod
    def calculate(cls, expression: str) -> float:
        """Return the result of evaluating the expression."""

        if cls._is_valid_expression(expression):
            expression = expression.replace('^', '**')
            return eval(expression)


if __name__ == '__main__':
    print(MathExpressionExecutor.calculate('3^3'))
