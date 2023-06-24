from input_parser import InputParser
from analyzer import Analyzer
from board import Board
from concurrent.futures import ThreadPoolExecutor
import threading as th


class ProcessController:
    def __init__(self, n_threads: int, board_sets: list[tuple[int, list[str]]]) -> None:
        self.__sem = th.Semaphore(n_threads)
        self.__n_threads = n_threads
        self.__threads = [th.Thread() for i in range(n_threads)]
        self.__board_sets = board_sets

    def start(self) -> None:

        tasks = [self.__process_row, self.__process_col, self.__process_region]
        max_tasks = len(self.__board_sets) * 3
        task_counter = 0

        while (task_counter != max_tasks):
            for thread in self.__threads:
                if not thread.is_alive():
                    thread.run(target=tasks[task_counter % 3],
                               args=self.board_sets[task_counter // 3])
                    task_counter += 1

            for thread in self.__threads:
                thread.join()

    def __process_row(self):
        pass

    def __process_col(self):
        pass

    def __process_region(self):
        pass

    def print_errors(self):
        pass
