class Report:
    def __init__(self, coq_output, r_output, status_code, line_number) -> None:
        self.coq_output = coq_output
        self.r_output = r_output
        self.status_code = status_code
        self.line_number = line_number


