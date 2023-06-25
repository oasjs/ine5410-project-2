import threading as th
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor

from analyzer import Analyzer


class ProcessController(Process):
    def __init__(self, n_threads: int,
                 board_sets: list[tuple[int, list[str]]]) -> None:
        super().__init__()
        self.__n_threads = n_threads
        self.__board_sets = board_sets
        self.__boards_errors = [[] for i in range(len(board_sets))]
        self._name = self._name[-1]

    def run(self) -> None:

        tasks = [self.__process_row, self.__process_col, self.__process_region]
        max_tasks = len(self.__board_sets) * 3
        task_counter = 0

        with ThreadPoolExecutor(max_workers=self.__n_threads) as e:
            while (task_counter != max_tasks):
                current_board = task_counter // 3
                current_task = task_counter % 3

                errors = e.submit(tasks[current_task],
                                  args=(self.__board_sets[current_board],))
                self.__boards_errors[current_board].append(errors)

                if (current_task == 0):
                    board_num = self.__board_sets[current_board][0]
                    print(
                        f'Processo {self._name}: resolvendo quebra-cabeças {board_num}')

                task_counter += 1

        for error_set in self.__boards_errors:
            board_errors: list[tuple[str, int]] = [
                err.result() for err in error_set]

            num_errors = 0
            for pair in board_errors:
                num_errors += pair[1]

            e = "; ".join([er[0] for er in board_errors])
            e = f' ({e})' if num_errors > 0 else ""
            print(
                f'Processo {self._name}: {num_errors} erros encontrados{e}')

    def __process_row(self, args: tuple[int, list[str]]) -> tuple[str, int]:
        board_set = args[0][1]
        thread_name = 'T'+th.current_thread().name[-1]
        analyzer = Analyzer(board_set)
        errors = analyzer.process_row()
        return (f'{thread_name}: {", ".join(errors)}', len(errors))

    def __process_col(self, args: tuple[int, list[str]]) -> tuple[str, int]:
        board_set = args[0][1]
        thread_name = 'T'+th.current_thread().name[-1]
        analyzer = Analyzer(board_set)
        errors = analyzer.process_col()
        return (f'{thread_name}: {", ".join(errors)}', len(errors))

    def __process_region(self, args: tuple[int, list[str]]) -> tuple[str, int]:
        board_set = args[0][1]
        thread_name = 'T'+th.current_thread().name[-1]
        analyzer = Analyzer(board_set)
        errors = analyzer.process_region()
        return (f'{thread_name}: {", ".join(errors)}', len(errors))
