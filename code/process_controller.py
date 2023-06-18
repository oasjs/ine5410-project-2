from input_parser import InputParser
from analyzer import Analyzer
from board import Board


class ProcessController:
    def __init__(self, n_threads: int, board_sets: list[list[str]]) -> None:
        self.__parser = InputParser()
        self.__analyzer = Analyzer()

    def start(self) -> None:
        for i in range(len(self.__board_sets)):
            board: Board = self.__parser.create_board(self.__board_sets[i])
            self.__analyzer.start(board)
