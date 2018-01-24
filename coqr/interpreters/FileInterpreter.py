import os
import re
import time
from typing import Dict, List

from coqr.interpreters import AbstractInterpreter
from coqr.parsing import parse
from coqr.reports.interpretation import Report, generate_sub_reports, SubReport
from coqr.utils import reports
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

    def interpret_directory(self, directory, recursive=False) -> List[Dict]:
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
        rsettings = os.path.join(directory, 'RSettings')
        if os.path.isfile(rsettings):
            with open(rsettings) as settings_:
                strat = settings_.readline()

            self.strategy = self.strategies.get(strat, self.interpret_multiline)

    def interpret_multiline(self, filename) -> List[Report]:
        parsed = parse.parse_file(filename)
        split_ = list(zip(*parsed))
        lines = split_[0]
        expressions = split_[1]

        outputs = self.interpreter.interpret_expressions(expressions)

        results = []

        for (expression, output, exec_time), line in zip(outputs, lines):
            sub_report = SubReport(expression, output, exec_time)
            results.append(Report(expression, filename, self.interpreter.name, line=line, sub_reports=[sub_report]))

        return results

    def interpret_line_by_line(self, filename: str) -> List[Report]:
        lines = read_file(filename)
        results = []
        # None filters blank lines
        for i, line in enumerate(filter(None, lines)):
            expressions = parse.parse_expression(line)
            outputs = self.interpreter.interpret_expressions(expressions)

            sub_reports = generate_sub_reports(outputs)
            results.append(Report(line, filename, self.interpreter.name, line=i + 1, sub_reports=sub_reports))

        return results
