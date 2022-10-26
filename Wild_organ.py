from Organ import Organ


class Wild_organ(Organ):

    def __init__(self, *args):
        super().__init__(*args)
        self.id = 3

    def __str__(self):
        return str(self.id)