import random
import numpy as np
import tkinter as tk
import time

environment = []
while np.sum(environment) <= 10:
    environment = np.array([[1 if random.random() < 0.5 else 0 for _ in range(4)] for _ in range(4)])


class VacuumAgent:
    def __init__(self):
        self.energy = 100
        self.bag = 0
        self.location = [0, 0]
        self.status = "off"

    def observe_environment(self):
        return environment[self.location[0], self.location[1]]

    def clean_dirt(self):
        if environment[self.location[0], self.location[1]] == 1:
            environment[self.location[0], self.location[1]] = 0
            self.bag += 1
            self.energy -= 1

    def empty_bag(self):
        self.bag = 0

    def determine_action(self):
        if self.status == "off":
            return None

        dirts = []
        for i in range(4):
            for j in range(4):
                if environment[i, j] == 1:
                    dirts.append([i, j])

        if self.bag == 10:
            self.return_home()
            self.empty_bag()

        elif dirts:
            closest_dirt = min(dirts, key=lambda x: abs(x[0] - self.location[0]) + abs(x[1] - self.location[1]))
            direction_x = closest_dirt[0] - self.location[0]
            direction_y = closest_dirt[1] - self.location[1]

            if direction_x > 0:
                return 'move_south'
            elif direction_x < 0:
                return 'move_north'
            elif direction_y > 0:
                return 'move_east'
            elif direction_y < 0:
                return 'move_west'
            else:
                return 'clean'
        else:
            self.return_home()

