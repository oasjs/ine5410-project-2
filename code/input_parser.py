from board import Board

# TODO: Implementar lógiica de percorrimento do tabuleiro


class InputParser:
    def __init__(self):
        self.__board: Board = Board()

    def remove_line_breaks(self, board_set: list[str]) -> list[str]:
        for i in range(len(board_set)):
            board_set[i] = board_set[i].replace("\n", "")
            print(board_set[i])
        print('Fim do print do Remove Line Breaks\n')
        return board_set

    def row_parser(self) -> list[str]:
        pass

    def col_parser(self):
        pass

    def region_parser(self):
        pass
