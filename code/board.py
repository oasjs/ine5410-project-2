# TODO: Implementar o tabuleiro com 3 versões: row-major, col-major, region-major


class Board:
    def __init__(self, id: int, rows: list[str]) -> None:
        self.id = id
        self.rows = rows
