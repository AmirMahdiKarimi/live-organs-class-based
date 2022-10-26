from time import sleep
import os

from Organ import Organ
from Wild_organ import Wild_organ
from Food import Food
from Controller import Controller
from Environment import Environment
from Eye import Eye
from Muscle import Muscle


if __name__ == '__main__':
    env = Environment(10)
    controller = Controller(env)

    Organ(controller, 0, 5, 15, 25, Eye(), Muscle())
    Organ(controller, 5, 8, 15, 25, Eye(), Muscle())
    Organ(controller, 0, 0, 15, 25, Eye(), Muscle())
    Wild_organ(controller, 5, 4, 12, 30, Eye(), Muscle())

    food1 = Food(controller, 9, 8)


    step = 0
    while True:
        print(f"**  {step}  **")
        print(controller.env)
        controller.update()

        # print("----------------------------------------------------")
        sleep(0.5)
        os.system('cls')
        # controller.set_random_food() if step % 2 == 0 else None
        step += 1
