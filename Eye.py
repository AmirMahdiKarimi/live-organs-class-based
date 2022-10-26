from random import randint
from Food import Food


class Eye:

    def __init__(self, sight_range=2):
        self.sight_range = sight_range

    def zone_maker(self, xy, tbl_size):
        zone = list(range(xy - self.sight_range, min(xy + self.sight_range + 1, tbl_size)))
        end_zone = (xy + self.sight_range + 1) % tbl_size if (xy + self.sight_range + 1) >= tbl_size else 0
        zone.extend(list(range(0, end_zone)))
        return zone

    def sight(self, organ):
        # radius = 0
        # while radius < self.sight_range:
        #     radius += 1
        #     r_near = []
        # r_near.extend(organ.controller.env.table[organ.x-radius:organ.x+radius+1][organ.y-radius])
        # r_near.extend(organ.controller.env.table[organ.x-radius:organ.x+radius+1][organ.y+radius])
        # r_near.extend(organ.controller.env.table[organ.x-radius][organ.y-radius+1:organ.y+radius])
        # r_near.extend(organ.controller.env.table[organ.x+radius][organ.y-radius+1:organ.y+radius])

        # for i in r_near:
        #     if r_near[i] != 0 and r_near[i].id < organ.id:
        #         organ.muscle.move(organ, )

        # for i in range(-radius, radius):
        #     if organ.controller.env.table[organ.x-radius][i] == :
        #
        #     if organ.controller.env.table[organ.x+radius][i]:
        #     if organ.controller.env.table[i][organ.y+radius]:
        #     if organ.controller.env.table[i][organ.y+radius]:

        # near_cells = organ.controller.env.table[organ.x-self.sight_range: organ.x+self.sight_range+1]
        # near_cells = near_cells[:][organ.y-self.sight_range: organ.y+self.sight_range+1]
        tbl = organ.controller.env.table
        tbl_size = organ.controller.env.size
        horizontal_zone = self.zone_maker(organ.y, tbl_size)
        vertical_zone = self.zone_maker(organ.x, tbl_size)
        # print(horizontal_zone)
        # print(vertical_zone)
        near_cells = [[tbl[i][j] for j in horizontal_zone] for i in vertical_zone]

        # print(organ.id)
        # print(near_cells)
        near_x = 0
        near_y = 0
        distance = self.sight_range + 1
        for x in range(2 * self.sight_range + 1):
            for y in range(2 * self.sight_range + 1):
                if near_cells[x][y] != 0 and near_cells[x][y].id < organ.id:
                    dist = max(abs(self.sight_range - x), abs(self.sight_range - y))
                    if dist < distance:
                        distance = dist
                        near_x = x
                        near_y = y

        new_x = organ.x
        new_y = organ.y

        if distance == self.sight_range + 1:
            new_x += randint(-1, 1)
            new_y += randint(-1, 1)

        else:
            # new_x += 1 if self.sight_range < near_x else -1 if self.sight_range > near_x else 0
            if self.sight_range < near_x:
                new_x += 1
            elif self.sight_range > near_x:
                new_x -= 1

            # new_y += 1 if self.sight_range < near_y else -1 if self.sight_range > near_y else 0
            if self.sight_range < near_y:
                new_y += 1
            elif self.sight_range > near_y:
                new_y -= 1

        new_x %= tbl_size
        new_y %= tbl_size
        organ.muscle.move(organ, new_x, new_y)
