
from board import Board

if __name__ == "__main__":
    b = Board()

    convert = {0: "UP", 1: "DOWN", 2: "LEFT", 3: "RIGHT"}

    test_board = [[0, 0, 1, 1],
                  [3, 3, 2, 1],
                  [0, 0, 0, 1],
                  [1, 1, 1, 1]]

    print("Testing:")
    b.set_board(test_board)
    b.print_board()
    print("")

    for move in range(4):
            
            b.set_board(test_board)

            print(convert[move])
            b.move(move)
            b.print_board()
            print("")
