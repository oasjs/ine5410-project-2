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
        tabuleiro_region_major = []
        region = ""
        tabuleiro_row_major = self.remove_line_breaks(["534678912\n", "672195348\n", "198342567\n", "859761423\n", "426853791\n", "713924856\n", "961537284\n", "287419635\n", "345286179\n"])
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for k in range(3):
                    for l in range(3):
                        region += tabuleiro_row_major[i+k][j+l]
                print(region)
                tabuleiro_region_major.append(region)
                region = ""
        pass

# Teste de execução do método remove_line_breaks
print('\nTeste de execução do método remove_line_breaks')
InputParser().remove_line_breaks(["123\n", "456\n", "789\n"])

# Teste de execução do método parse_row
print('\nTeste de execução do método parse_row')
InputParser().row_parser()

# Teste de execução do método parse_col
print('\nTeste de execução do método parse_col')
InputParser().col_parser()

# Teste de execução do método parse_region
print('\nTeste de execução do método parse_region')
InputParser().region_parser()