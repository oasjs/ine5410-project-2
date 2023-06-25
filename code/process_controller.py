import threading as th
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor

from analyzer import Analyzer


class Error:
    def __init__(self, thread_name: str, errors: list[str], num_errors: int):
        self.__thread_name = thread_name
        self.__errors = errors
        self.__num_errors = num_errors

    @property
    def thread_name(self) -> str:
        return self.__thread_name

    @property
    def errors(self) -> list[str]:
        return self.__errors

    @property
    def num_errors(self) -> int:
        return self.__num_errors


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
            board_errors: list[Error] = [e.result() for e in error_set]

            num_errors = 0
            thread_errors = {e.thread_name: []
                             for e in board_errors if e.num_errors > 0}

            for e in board_errors:
                num_errors += e.num_errors
                if e.num_errors > 0:
                    thread_errors[e.thread_name].extend(e.errors)

            r = [f'{k}: {", ".join(v)}' for k, v in thread_errors.items()]
            r = f' ({"; ".join(r)})' if num_errors > 0 else ''
            f = f'Processo {self._name}: {num_errors} erros encontrados{r}'
            print(f)

    def __process_row(self, args: tuple[int, list[str]]) -> Error:
        board_set = args[0][1]
        thread_name = 'T' + str(int(th.current_thread().name[-1]) + 1)
        analyzer = Analyzer(board_set)
        errors = analyzer.process_row()
        return Error(thread_name, errors, len(errors))

    def __process_col(self, args: tuple[int, list[str]]) -> Error:
        board_set = args[0][1]
        thread_name = 'T' + str(int(th.current_thread().name[-1]) + 1)
        analyzer = Analyzer(board_set)
        errors = analyzer.process_col()
        return Error(thread_name, errors, len(errors))

    def __process_region(self, args: tuple[int, list[str]]) -> Error:
        board_set = args[0][1]
        thread_name = 'T' + str(int(th.current_thread().name[-1]) + 1)
        analyzer = Analyzer(board_set)
        errors = analyzer.process_region()
        return Error(thread_name, errors, len(errors))
