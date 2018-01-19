import re
from abc import ABC, abstractmethod


class AbstractInterpreter(ABC):
    SEQUENCE_TOKEN = "; 'TOKEN' ;"
    token_regex = re.compile(r'\[\d\]\s*"TOKEN"\s*')

    def __init__(self, interp) -> None:
        self.name = ''
        self.interpreter = interp

    @abstractmethod
    def interpret_expressions(self, expressions: list):
        pass

    @abstractmethod
    def interpret(self, expression) -> str:
        pass
