from Organ import Organ

class Environment:

    def __init__(self, size=100):
        self.size = size
        self.table = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.organs = []

    def get_emoji(self, index):
        emoji = ["0", "1", "2", "3"]
        # emoji = ["\U0001f600", "\U0001F444", "2", "\U0001F608"]
        return emoji[index]

    def __str__(self):
        return "\n".join([str(" ".join([str((item if item == 0 else item.id)) for item in row])) for row in self.table])

    def empty_cells(self):
        empty = []
        for i in range(self.size):
            for j in range(self.size):
                if self.table[i][j] == 0:
                    empty.append((i, j))
        return empty
