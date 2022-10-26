

class Food:

    def __init__(self, controller, x: int, y: int, energy: int = 4, life_span: int = 8):
        self.id = 1
        self.controller = controller
        self.energy = energy
        self.life_span = life_span
        self.x, self.y = x, y
        self.controller.set_food(self)

    def is_alive(self):
        if self.life_span > 0 :
            return True
        else:
            return False

    def __str__(self):
        return str(self.id)