import sys
from process_controller import ProcessController


def main() -> int:

    if (len(sys.argv)) < 4:
        print("Você deve informar o nome do arquivo de entrada e o número de processos e threads!")
        return 1

    file = sys.argv[1]
    n_processes = int(sys.argv[2])
    n_threads = int(sys.argv[3])

    if (n_processes <= 0 or n_threads <= 0):
        print("Números de processos e threads devem ser maior do que 0!")
        return 1

    with open(file, 'r') as f:
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

    processes = []
    for i in range(n_processes):
        start = prev_end
        end = prev_end + step + 1 if mod > 0 else prev_end + step
        board_sets = input[start:end]

        prev_end = end
        if mod > 0:
            mod -= 1

        pc = ProcessController(n_threads, board_sets)
        processes.append(pc)
        pc.start()
        if __name__ != '__main__':
            return 0

    for process in processes:
        process.join()

    return 0


if __name__ == '__main__':
    main()
