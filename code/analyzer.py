from typing import Any
from board import Board

# TODO: Implementar verificação dos erros para cada tipo de perocrrimento

class Analyzer:
    def __init__(self) -> None:
        pass

    def start(self, board : Board):
        errors = list()

        # Verifica erros nas linhas
        for i in range(9):
            e = self.check(board.row_major[i])
            if e:
                errors.append(f"L{i+1}")

        # Verifica erros nas colunas
        for i in range(9):
            e = self.check(board.col_major[i])
            if e:
                errors.append(f"C{i+1}")

        # Verifica erros nas regiões
        for i in range(9):
            e = self.check(board.region_major[i])
            if e:
                errors.append(f"R{i+1}")
        
        return errors
           
    def check(self, board : str):
        errors = 0
        # Verificar o número de caracteres repetidos
        for c in board:
           count = board.count(c)
           if count > 1:
               errors += count - 1
        return errors
    