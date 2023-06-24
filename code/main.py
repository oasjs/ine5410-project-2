import sys
from concurrent.futures import ProcessPoolExecutor
from process_controller import ProcessController
from input_parser import InputParser


def main() -> int:

    if (len(sys.argv)) < 3:
        print("Você deve informar o número de processos e threads!")
        return 1

    n_processes = int(sys.argv[1])
    n_threads = int(sys.argv[2])

    if (n_processes <= 0 or n_threads <= 0):
        print("Números de processos e threads devem ser maior do que 0!")
        return 1

    with open('input-sample.txt', 'r') as f:
        input = f.readlines()

    # Divide input em tabuleiros, pulando as quebras de linha do arquivo, e
    # incluindo os identificadores dos tabuleiros
    input = [(i // 10, input[i:i+9]) for i in range(0, len(input), 10)]
    n_boards = len(input)

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

            e.submit(ProcessController(n_threads, board_sets).start)

    return 0


main()
