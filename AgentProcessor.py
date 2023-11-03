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

def execute_action(self, action):
        if self.status == "off":
            return

        if action == 'move_north':
            if self.location[0] > 0:
                self.location[0] -= 1
        elif action == 'move_south':
            if self.location[0] < 3:
                self.location[0] += 1
        elif action == 'move_east':
            if self.location[1] < 3:
                self.location[1] += 1
        elif action == 'move_west':
            if self.location[1] > 0:
                self.location[1] -= 1
        elif action == 'clean':
            self.clean_dirt()
        elif action == 'return_home':
            self.return_home()

        if action is not None:
            self.energy -= 1

def return_home(self):
    while self.location != [0, 0] and self.energy > 0:
        if self.location[0] > 0:
            self.location[0] -= 1
        else:
            self.location[1] -= 1
        self.energy -= 1
        #atualiza interface
        time.sleep(1)

def iterate():
    if agent.energy > 0:
        #atualiza interface
        if agent.bag <= 10:
            action = agent.determine_action()
            agent.execute_action(action)
            #atualiza interface
            root.after(1000, iterate)
        else:
            agent.return_home()
            agent.empty_bag()
            action = agent.determine_action()
            agent.execute_action(action)
            #atualiza interface
            root.after(1000, iterate)


iterate()

agent = VacuumAgent()

class GUIInterface:
    def __init__(self, root, agent):
        self.root = root
        self.agent = agent

        self.status_label = tk.Label(root, text=f"Status:{self.agent.status}")
        self.status_label.pack()

        self.toggle_button = tk.Button(root, text="Turn On/Off", command=self.toggle_status)
        self.toggle_button.pack()

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.info_label = tk.Label(root, text="")
        self.info_label.pack()


    def toggle_status(self):
        if self.agent.status == "on":
            self.agent.status = "off"
            self.status_label.config(text="Status: Off")
        else:
            self.agent.status = "on"
            self.status_label.config(text="Status: On")
            
            
            
            
    def update_interface(self):
        self.canvas.delete("all")
        for i in range(4):
            for j in range(4):
                color = "white" if environment[i, j] == 0 else "black"
                self.canvas.create_rectangle(j * 100, i * 100, (j + 1) * 100, (i + 1) * 100, fill=color)
        agent_color = "red" if environment[self.agent.location[0], self.agent.location[1]] == 1 else "orange"
        self.canvas.create_rectangle(self.agent.location[1] * 100, self.agent.location[0] * 100,
                                     (self.agent.location[1] + 1) * 100, (self.agent.location[0] + 1) * 100,
                                     fill=agent_color)

        self.info_label.config(
            text=f"Energia: {self.agent.energy}, Bag: {self.agent.bag}, Full: {'Yes' if self.agent.bag == 10 else 'No'}")
        self.root.update_idletasks()        


if __name__ == "__main__":
    root = tk.Tk()
    agent = VacuumAgent()
    GUIInterface(root, agent)
    root.mainloop()