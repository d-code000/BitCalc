from typing import Union


class Calculator:
    def __init__(self):
        self.first_num: Union[int | None] = None
        self.second_num: Union[int | None] = None
        self.operation: Union[str | None] = None
        self.memory: int = 0

    def get_result(self) -> int:
        if self.first_num is not None and self.second_num is not None and self.operation:
            match self.operation:
                case '+': result = self.first_num + self.second_num
                case '-': result = self.first_num - self.second_num
                case '*': result = self.first_num * self.second_num
                case '/': result = self.first_num / self.second_num
                case '**': result = self.first_num ** self.second_num
                case _: raise TypeError("Invalid operation")
            return round(result)
        raise SyntaxError("All parameters are not set")

    def clear(self) -> None:
        self.first_num = None
        self.second_num = None
        self.operation = None
