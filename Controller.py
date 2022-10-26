from random import randint

from Wild_organ import Wild_organ
from Environment import Environment
from Eye import Eye
from Food import Food
from Muscle import Muscle
from Organ import Organ


class Controller:
    def __init__(self, env: Environment):
        self.env = env

    def add_organ(self, organ):
        self.get_organs().append(organ)

    def set_organ(self, organ):
        self.env.table[organ.x][organ.y] = organ

    #  -- random set organ --
    #     empty_cells = self.env.empty_cells()
    #     if len(empty_cells) == 0:
    #         raise print("organ not added!")
    #     else:
    #         location = empty_cells[randint(0, len(empty_cells)-1)]
    #         return location[0], location[1]

    def random_loc(self):
        empty_cells = self.env.empty_cells()
        # if len(empty_cells) == 0:
        #     raise print("organ not added!")
        # else:

        if len(empty_cells) != 0:
            location = empty_cells[randint(0, len(empty_cells) - 1)]
            return location[0], location[1]

    def get_organs(self):
        return self.env.organs

    def set_random_food(self):
        empty_cells = self.env.empty_cells()
        if len(empty_cells) != 0:
            location = empty_cells[randint(0, len(empty_cells) - 1)]
            self.env.table[location[0]][location[1]] = Food(self, location[0], location[1])

    def can_go(self, x, y, organ):
        return 0 if self.env.table[x][y] == 0 else self.env.table[x][y].id

    def add_energy(self, x, y):
        if self.env.table[x][y] == 0:
            return 0
        return self.env.table[x][y].energy

    def set_food(self, food):
        self.env.table[food.x][food.y] = food

    def clean_cell(self, x, y):
        self.env.table[x][y] = 0

    def remove_organ(self, x, y):
        if self.env.table[x][y] != 0 and self.env.table[x][y].id > 1:
            self.get_organs().remove(self.env.table[x][y])

    def organ_to_food(self, organ):
        self.env.table[organ.x][organ.y] = Food(self, organ.x, organ.y)

    def update(self):
        if len(self.get_organs()) == 0:
            exit()
        for org in self.get_organs():
            org.energy -= 1
            org.life_span -= 1
            org.eye.sight(org)
            # print(f"{org.id}: {org.energy}")
            if org.energy <= 0 or org.life_span <= 0:
                self.remove_organ(org.x, org.y)
                self.organ_to_food(org)

        for org in self.get_organs():
            self.born_organ(org) if org.id == 2 and org.energy >= org.MAX_ENERGY / 2 else None
            self.born_organ(org) if org.id == 3 and org.energy >= org.MAX_ENERGY * 2 / 3 else None

        if len(self.get_organs()) <= self.env.size * self.env.size * 9 / 10:
            for i in range(int(len(self.get_organs()) / 2)):
                self.set_random_food()

    def born_organ(self, organ):
        child_energy = int(organ.MAX_ENERGY / 3) if organ.energy >= 2 * int(
            organ.MAX_ENERGY / 3) else organ.energy - int(organ.MAX_ENERGY / 3)
        organ.energy -= child_energy
        x, y = self.random_loc()
        organ_type = Organ if organ.id == 2 and randint(0, 1) == 0 else Wild_organ if randint(0, 3) == 0 else Organ
        life_span = randint(12, 18) if organ.id == 2 else randint(4, 8)
        organ_type(organ.controller, x, y, child_energy, life_span, Eye(), Muscle())
