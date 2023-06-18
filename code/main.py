import sys
from concurrent.futures import ProcessPoolExecutor
from process_controller import ProcessController
from input_parser import InputParser


def main() -> int:
    n_processes = int(sys.argv[1])
    n_threads = int(sys.argv[2])

    if (len(sys.argv)) < 3:
        print("Tá errado!")
        return 1

    with open('input-sample.txt', 'r') as f:
        input = f.readlines()

    # Remove os elementos quebra-de-linha da lista
    input = [i for i in input if i != '\n']

    n_boards = len(input) // 9

    # Divide input em tabuleiros
    input = [input[i:i+9] for i in range(0, len(input), 9)]

    # Limita o número máximo de processos ao número de tabuleiros
    if n_processes > n_boards:
        n_processes = n_boards

    # Inicaliza as variáveis para a distribuição de pombal
    step = n_boards // n_processes
    mod = n_boards % n_processes
    prev_end = 0

    with ProcessPoolExecutor(max_workers=n_processes) as e:
        for i in range(n_processes):
            start = prev_end
            end = prev_end + step + 1 if mod > 0 else prev_end + step
            board_sets = input[start:end]

            prev_end = end
            if mod > 0:
                mod -= 1

            e.submit(ProcessController(n_threads, board_sets).start())

    return 0


main()
