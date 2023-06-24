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
            c = self.check(board.row_major[i])
            for e in c:
                errors.append(f"L{e}")

        # Verifica erros nas colunas
        for i in range(9):
            c = self.check(board.col_major[i])
            for e in c:
                errors.append(f"C{e}")

        # Verifica erros nas regiões
        for i in range(9):
            c = self.check(board.region_major[i])
            for e in c:
                errors.append(f"R{e}")
        
        return errors
           
    def check(self, board : str):
        errors = list()
        # Verificar os caracteres repetidos e guarda a posição do erro
        for i in range(9):
            for j in range(i+1, 9):
                if board[i] == board[j]:
                    errors.append(j+1)
        return errors