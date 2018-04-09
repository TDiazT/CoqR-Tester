import os
import re
from typing import Dict, List

from coqr.interpreters import AbstractInterpreter
from coqr.parsing import parse
from coqr.reports.interpretation import Report, generate_sub_reports, InterpretationResult
from coqr.utils.file import read_file


class FileInterpreter:
    settings_regex = re.compile(r'\@(\w+)')

    def __init__(self, interpreter: AbstractInterpreter) -> None:
        super().__init__()
        self.interpreter = interpreter
        self.strategy = self.interpret_multiline
        self.strategies = {
            'line': self.interpret_line_by_line,
            'multi': self.interpret_multiline
        }

    def interpret_file(self, filename):
        results = []
        current_strategy = self.strategy
        self.__set_file_strategy(filename)

        result = self.strategy(filename)
        results.extend(result)

        self.strategy = current_strategy

        return results

    def interpret_directory(self, directory, recursive=False) -> List[Report]:
        results = []
        files = os.listdir(directory)

        self.__set_dir_strategy(directory)

        for f in files:
            print("Interpreting file %s" % f)
            file_ = os.path.join(directory, f)
            if os.path.isdir(file_):
                if recursive:
                    current_strategy = self.strategy
                    results.extend(self.interpret_directory(file_))
                    self.strategy = current_strategy
            if os.path.isfile(file_):
                if file_.endswith('.R'):
                    current_strategy = self.strategy
                    self.__set_file_strategy(file_)

                    result = self.strategy(file_)
                    results.extend(result)

                    self.strategy = current_strategy

        return results

    def __set_file_strategy(self, filename):
        with open(filename) as file_:
            line = file_.readline()
        tag = self.settings_regex.search(line)
        if tag:
            strategy = tag.group(1)
            self.strategy = self.strategies.get(strategy, self.strategy)

    def __set_dir_strategy(self, directory):
        r_settings = os.path.join(directory, 'RSettings')
        if os.path.isfile(r_settings):
            with open(r_settings) as settings_:
                strategy = settings_.readline()

            self.strategy = self.strategies.get(strategy, self.interpret_multiline)

    def interpret_multiline(self, filename) -> List[Report]:
        parsed = parse.parse_file(filename)
        split_ = list(zip(*parsed))
        lines = split_[0]
        expressions = split_[1]

        outputs = self.interpreter.interpret_expressions(expressions)

        results = []

        for (expression, output, exec_time), line in zip(outputs, lines):
            sub_report = InterpretationResult(expression, output, exec_time)
            results.append(Report(expression, os.path.basename(filename), self.interpreter.name, line=line, sub_reports=[sub_report]))

        return results

    def interpret_line_by_line(self, filename: str) -> List[Report]:
        lines = read_file(filename)
        results = []
        # None filters blank lines
        for i, line in enumerate(filter(None, lines)):
            print("Interpreting line %i" % i)
            expressions = parse.parse_expression(line)
            outputs = self.interpreter.interpret_expressions(expressions)

            sub_reports = generate_sub_reports(outputs)
            results.append(Report(line, os.path.basename(filename), self.interpreter.name, line=i + 1, sub_reports=sub_reports))

        return results
