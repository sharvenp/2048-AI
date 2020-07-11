
class Controller:

    def __init__(self, board):
        self.board = board

    def handle(self):
        raise NotImplementedError