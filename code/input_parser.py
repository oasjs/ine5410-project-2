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
        return self.remove_line_breaks(["534678912\n", "672195348\n", "198342567\n", "859761423\n", "426853791\n", "713924856\n", "961537284\n", "287419635\n", "345286179\n"])

    def col_parser(self) -> list[str]:
        tabuleiro_col_major = []
        column = ""
        tabuleiro_row_major = self.remove_line_breaks(["534678912\n", "672195348\n", "198342567\n", "859761423\n", "426853791\n", "713924856\n", "961537284\n", "287419635\n", "345286179\n"])
        for i in range(9):
            for j in range(0, 9):
                column += tabuleiro_row_major[j][i]
            print(column)
            tabuleiro_col_major.append(column)
            column = ""

    def region_parser(self):
        pass
