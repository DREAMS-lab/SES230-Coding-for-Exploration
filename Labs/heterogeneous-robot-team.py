import numpy as np

class Robot:
    def __init__(self, id, x,y,z):
        self.id = id
        self.x = x
        self.y = y
        self.z = z

    def move(self):
        return self.id, self.getPose()

    def getPose(self):
        return self.x, self.y, self.z

    def getID(self):
        return self.id


class AirDrone(Robot):
    def __init__(self, id, x, y):
        Robot.__init__(self, id, x, y, 0.2) # z-offset: the drone is just a little above ground

    def move(self):
        self.x = self.x+np.random.normal(1,2)
        self.y = self.y+np.random.normal(1,2)
        self.z = self.z+np.random.normal(1,1)
        return self.id, self.getPose()


class RobotBoat(Robot):
    def __init__(self, id, x, y):
        Robot.__init__(self, id, x, y, 0)

    def move(self):
        self.x = self.x + np.random.normal(1,2)
        self.y = self.y + np.random.normal(1,2)
        return self.id, self.getPose()


class UnderwaterDrone(Robot):
    def __init__(self, id, x, y):
        Robot.__init__(self, id, x, y, -0.2)

    def move(self):
        self.x = self.x + np.random.normal(1,3)
        self.y = self.y + np.random.normal(1,3)
        self.z = self.z - np.random.normal(1,1)
        return self.id, self.getPose()

import matplotlib.pyplot as plt
robots = [(UnderwaterDrone('uDrone', 0, 0)), (AirDrone('eagle', 0, 0)), (RobotBoat('robo-boat-o', 0, 0))]

poses = {}
for robot in robots:
    poses[robot.getID()] = []

for step in range(0,100):
    # move the robot
    for robot in robots:
        id, pose = robot.move()
        poses[id].append(pose)

pose_list = [np.array(poses['uDrone']), np.array(poses['eagle']),np.array(poses['robo-boat-o'])]

fig = plt.figure()
ax = plt.axes(projection='3d')
for pose_vec in pose_list:
        xdata = pose_vec[:, 0]
        ydata = pose_vec[:, 1]
        zdata = pose_vec[:, 2]
        ax.scatter3D(xdata, ydata, zdata, c=zdata)


plt.show()


