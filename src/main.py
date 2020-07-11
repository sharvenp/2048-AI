
from board import Board
from view import View
from human_controller import HumanController

if __name__ == "__main__":
    b = Board()
    v = View()
    c = HumanController(b)
    
    v.attach_controller(c)
    b.add_observer(v)

    v.launch()