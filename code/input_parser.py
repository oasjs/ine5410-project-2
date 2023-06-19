from board import Board

# TODO: Implementar lógiica de percorrimento do tabuleiro


class InputParser:
    def __init__(self, board: list[str]):
        self.__input = self.remove_line_breaks(board.copy())
        self.__board = Board()

    @property
    def board(self) -> Board:
        return self.__board

    def remove_line_breaks(self, board_set: list[str]) -> list[str]:
        for i in range(len(board_set)):
            board_set[i] = board_set[i].replace("\n", "")
        return board_set

    def row_parser(self) -> list[str]:
        return self.__input

    def col_parser(self) -> list[str]:
        tabuleiro_col_major = []
        column = ""
        tabuleiro_row_major = self.__input
        for i in range(9):
            for j in range(0, 9):
                column += tabuleiro_row_major[j][i]
            tabuleiro_col_major.append(column)
            column = ""
        return tabuleiro_col_major

    def region_parser(self):
        tabuleiro_region_major = []
        region = ""
        tabuleiro_row_major = self.remove_line_breaks(self.__input)
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for k in range(3):
                    for l in range(3):
                        region += tabuleiro_row_major[i+k][j+l]
                tabuleiro_region_major.append(region)
                region = ""
        return tabuleiro_region_major

