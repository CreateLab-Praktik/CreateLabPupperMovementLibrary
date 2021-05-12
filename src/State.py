import numpy as np
from enum import Enum


class State:
    def __init__(self):
        self.horizontal_velocity = np.array([0.0, 0.0])
        self.yaw_rate = 0.0
        self.height = -0.16
        self.pitch = 0.0
        self.roll = 0.0
        self.activation = 0
        self.behavior_state = BehaviorState.REST

        self.ticks = 0
        self.foot_locations = np.zeros((3, 4))
        self.joint_angles = np.zeros((3, 4))

    def behaviorStateAsString(self):
        if self.behavior_state == BehaviorState.REST:
            return"Robot in REST mode"
        elif self.behavior_state == BehaviorState.TROT:
            return"Robot in TROT mode"
        elif self.behavior_state == BehaviorState.HOP:
            return"Robot in HOP mode"
        else:
            return"Robot in DEACTIVATED mode"
    
    def printSelf(self):
        print("""
        Robot state print: \n   
        height = """, self.height, " \n "
        "yaw_rate = ", self.yaw_rate, " \n "
        "pitch = ", self.pitch, " \n "
        "roll = ", self.roll, " \n "
        "activation = ", self.activation, " \n "
        "ticks = ", self.ticks, " \n "
        "mode = ",self.behaviorStateAsString(), "\n"
        ,)


        


class BehaviorState(Enum):
    DEACTIVATED = -1
    REST = 0
    TROT = 1
    HOP = 2
    FINISHHOP = 3