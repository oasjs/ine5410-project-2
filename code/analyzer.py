from board import Board

# TODO: Implementar lógiica de percorrimento do tabuleiro


class Analyzer:
    def __init__(self, board_set: list) -> None:
        self.__board = self.remove_line_breaks(board_set.copy())

    def remove_line_breaks(self, board_set: list[str]) -> list[str]:
        for i in range(len(board_set)):
            board_set[i] = board_set[i][:9]
        return board_set

    def process_row(self) -> list[str]:
        b = self.__board
        errors = list()
        # Verifica erros nas linhas
        for i in range(9):
            e = self.__analyze(b[i])
            if e:
                errors.append(f"L{i+1}")
        return errors

    def process_col(self) -> list[str]:
        board_col_major = self.__parse_col(self.__board)
        errors = list()

        for i in range(9):
            e = self.__analyze(board_col_major[i])
            if e:
                errors.append(f"C{i+1}")
        return errors

    def process_region(self):
        board_region_major = self.__parse_region(self.__board)
        errors = list()
        # Verifica erros nas regiões
        for i in range(9):
            e = self.__analyze(board_region_major[i])
            if e:
                errors.append(f"R{i+1}")
        
        return errors
    
    def __parse_col(self, b):
        board_col_major = []
        column = ""
        for i in range(9):
            for j in range(9):
                column += b[j][i]
            board_col_major.append(column)
            column = ""
        return board_col_major
    
    def __parse_region(self, b):
        board_region_major = []
        region = ""
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for k in range(3):
                    for l in range(3):
                        region += b[i+k][j+l]
                board_region_major.append(region)
                region = ""
        return board_region_major
    
    # Analiza uma string e retorna o número de erros
    def __analyze(self, board : str) -> int:
        errors = 0
        # Verifica o número de caracteres repetidos
        for c in board:
           count = board.count(c)
           if count > 1:
               errors += count - 1
        return errors


# Testar o analyser
b = Analyzer([
    "534678912\n",
    "672195348\n",
    "198342567\n",
    "859761423\n",
    "426853791\n",
    "713924856\n",
    "961537284\n",
    "287419635\n",
    "345286179\n"])

# printa os erros
print(b.process_row())
print(b.process_col())
print(b.process_region())