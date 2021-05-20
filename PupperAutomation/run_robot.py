import numpy as np
import time
from src.Controller import Controller
from .MessageHandler import MessageHandler
from src.State import State
from pupper.HardwareInterface import HardwareInterface
from pupper.Config import Configuration
from pupper.Kinematics import four_legs_inverse_kinematics

def run_robot(connectionPipe, do_print = False):
    """
        A loop function cabable of updating a pupper robots state object based of of commands recieved via pipe form the transmission loop.
        
    """

    config = Configuration()
    hardware_interface = HardwareInterface()

    controller = Controller(
        config,
        four_legs_inverse_kinematics,
    )
    state = State()

    if do_print == True:
        print("Creating pipe connection...")
    msgHandler = MessageHandler(config, connectionPipe)
    if do_print == True:
        print("Done.")

    last_loop = time.time()
    deactivate = False

    while True:

        if deactivate == True:
            print("Robot loop terminated")
            break
        if do_print == True:
            print("Main robot loop")
        while True:
            print("Activation robot loop")
            command = msgHandler.get_command_from_pipe(state)
            if command.activate_event == 1:
                break
            time.sleep(0.1)
        if do_print == True:
            print("Robot activated.")

        while True:
            now = time.time()
            if now - last_loop < config.dt:
                continue
            last_loop = time.time()

            # Parse the udp joystick commands and then update the robot controller's parameters
            command = msgHandler.get_command_from_pipe(state)
            if command.activate_event == 1:
                deactivate = True
                if do_print == True:
                    print("Deactivating Robot")
                break

            # Read imu data. Orientation will be None if no data was available
            quat_orientation = np.array([1, 0, 0, 0])
            
            state.quat_orientation = quat_orientation

            # Step the controller forward by dt
            controller.run(state, command)
            if do_print == True:
                state.printSelf()

            # Update the pwm widths going to the servos
            hardware_interface.set_actuator_postions(state.joint_angles)
