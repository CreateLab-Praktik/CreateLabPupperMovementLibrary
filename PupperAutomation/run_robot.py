import numpy as np
import time
from src.Controller import Controller
from .MessageHandler import MessageHandler
from src.State import State
from pupper.HardwareInterface import HardwareInterface
from pupper.Config import Configuration
from pupper.Kinematics import four_legs_inverse_kinematics
from multiprocessing import connection

def run_robot(PipeConnection: connection.Connection, printState = False):
    """
        A loop function cabable of updating a pupper robots state object based of of commands recieved via pipe form the transmission loop.
        
    """

    config = Configuration()

    hardware_interface = HardwareInterface()

    controller = Controller(config, four_legs_inverse_kinematics,)

    state = State()

    msgHandler = MessageHandler(config, PipeConnection)


    last_loop = time.time()

    deactivate = False

    while True:

        if deactivate == True:
            print("Robot loop terminated")
            break

        while True:

            command = msgHandler.get_command_from_pipe(state)
            if command.activate_event == 1:
                break

            time.sleep(0.1)
            

        while True:

            now = time.time()
            if now - last_loop < config.dt:
                continue
            last_loop = time.time()

            command = msgHandler.get_command_from_pipe(state)
            if command.activate_event == 1:
                deactivate = True
                break

            state.quat_orientation = np.array([1, 0, 0, 0])

            # Step the controller forward by dt
            controller.run(state, command)
            if printState == True:
                state.printSelf()

            # Update the pwm widths going to the servos
            hardware_interface.set_actuator_postions(state.joint_angles)
