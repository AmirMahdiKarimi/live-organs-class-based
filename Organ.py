from Eye import Eye
from Muscle import Muscle


class Organ(Eye, Muscle):

    def __init__(self, controller, x: int, y: int, energy: int, life_span: int, eye: Eye, muscle: Muscle):
        self.id = 2
        self.controller = controller
        self.energy = energy
        self.life_span = life_span
        self.eye = eye
        self.muscle = muscle
        self.x, self.y = x, y
        self.controller.set_organ(self)
        self.controller.add_organ(self)
        self.MAX_ENERGY = 30

    def is_alive(self):
        if self.life_span > 0 and self.energy > 0:
            return True
        else:
            return False

    def __str__(self):
        return str(self.id)
