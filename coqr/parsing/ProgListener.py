from coqr.parsing.RParser import RParser

from coqr.parsing.RListener import RListener


class ProgListener(RListener):
    exps = []

    def __init__(self, stream) -> None:
        super().__init__()
        self.token_stream = stream

    def enterProg(self, ctx: RParser.ProgContext):
        for expr in ctx.expr():
            start_index = expr.start.tokenIndex
            stop_index = expr.stop.tokenIndex
            text = self.token_stream.getText(interval=(start_index, stop_index))
            self.exps.append(text)
