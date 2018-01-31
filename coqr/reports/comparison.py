class Report:
    def __init__(self, expression, status, dev_output, target_output, dev_processed_out, target_processed_out,
                 filename, dev_exec_time=-1, target_exec_time=-1, line='', context=''):
        super().__init__()
        self.expression = expression
        self.status_code = status
        self.dev_output = dev_output
        self.target_output = target_output
        self.dev_processed_out = dev_processed_out
        self.target_processed_out = target_processed_out
        self.dev_exec_time = dev_exec_time
        self.target_exec_time = target_exec_time
        self.line = line
        self.filename = filename
        self.context = context

    def to_json(self):
        return self.__dict__
