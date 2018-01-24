import re
from abc import ABC, abstractmethod
from typing import Tuple, List


class AbstractInterpreter(ABC):
    SEQUENCE_TOKEN = "; 'TOKEN' ;"
    token_regex = re.compile(r'\[\d\]\s*"TOKEN"\s*')

    def __init__(self, interp) -> None:
        self.name = ''
        self.interpreter = interp

    @abstractmethod
    def interpret_expressions(self, expressions: list) -> List[Tuple[str, str, int]]:
        """
        Interpret a list of expressions and returns a list with the expressions, their outputs and time it took to
        interpret
        :param expressions: List of strings
        :return: List of tuples containing expression, output and time
        """
        pass

    @abstractmethod
    def interpret(self, expression) -> str:
        """
        Interpret a expression and returns its output
        :param expression: String representing a expression
        :return: Output from interpreting that expression
        """
        pass
