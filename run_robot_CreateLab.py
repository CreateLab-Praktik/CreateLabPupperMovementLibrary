import numpy as np
import time
from src.Controller import Controller
from CommandMessageInterface_Pipe import CommandMessageInterface
from src.State import State
from pupper.HardwareInterface import HardwareInterface
from pupper.Config import Configuration
from pupper.Kinematics import four_legs_inverse_kinematics

def run_robot_CreateLab(connectionPipe, do_print = False):

    config = Configuration()
    hardware_interface = HardwareInterface()

    controller = Controller(
        config,
        four_legs_inverse_kinematics,
    )
    state = State()
    if do_print == True:
        print("Creating pipe connection...")
    cmdMsgInterface = CommandMessageInterface(config, connectionPipe)
    if do_print == True:
        print("Done.")

    last_loop = time.time()

    while True:
        if do_print == True:
            print("run_robot_loop")
        while True:
            command = cmdMsgInterface.get_command(state)
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
            command = cmdMsgInterface.get_command(state)
            if command.activate_event == 1:
                hardware_interface.deactivate_servos()
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
