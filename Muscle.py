class Muscle:
    def move(self, organ, new_x, new_y):
        destination_id = organ.controller.can_go(new_x, new_y, organ)
        if organ.id > destination_id:
            organ.energy -= 1 if organ.id == 3 and destination_id == 2 else 0
            organ.controller.clean_cell(organ.x, organ.y)
            organ.energy = min(organ.energy + organ.controller.add_energy(new_x, new_y), organ.MAX_ENERGY)
            organ.controller.remove_organ(new_x, new_y)
            organ.x = new_x
            organ.y = new_y
            organ.controller.set_organ(organ)
