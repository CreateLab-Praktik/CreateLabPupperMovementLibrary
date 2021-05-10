import numpy as np
import time
from src.IMU import IMU
from src.Controller import Controller
from CommandMessageInterface import CommandMessageInterface
from src.State import State
from pupper.HardwareInterface import HardwareInterface
from pupper.Config import Configuration
from pupper.Kinematics import four_legs_inverse_kinematics

def run_robot_CreateLab(use_imu=False):

    config = Configuration()
    hardware_interface = HardwareInterface()


    if use_imu:
        imu = IMU(port="/dev/ttyACM0")
        imu.flush_buffer()


    controller = Controller(
        config,
        four_legs_inverse_kinematics,
    )
    state = State()

    print("Creating udp listener...")
    cmdMsgInterface = CommandMessageInterface(config)
    print("Done.")

    last_loop = time.time()

    print("Summary of gait parameters:")
    print("overlap time: ", config.overlap_time)
    print("swing time: ", config.swing_time)
    print("z clearance: ", config.z_clearance)
    print("x shift: ", config.x_shift)


    while True:
        print("It is CreateLab running")
        while True:
            command = cmdMsgInterface.get_command(state)
            if command.activate_event == 1:
                break
            time.sleep(0.1)
        print("Robot activated.")

        while True:
            now = time.time()
            if now - last_loop < config.dt:
                continue
            last_loop = time.time()

            # Parse the udp joystick commands and then update the robot controller's parameters
            command = cmdMsgInterface.get_command(state)
            if command.activate_event == 1:
                print("Deactivating Robot")
                break

            # Read imu data. Orientation will be None if no data was available
            quat_orientation = (
                imu.read_orientation() if use_imu else np.array([1, 0, 0, 0])
            )
            state.quat_orientation = quat_orientation

            # Step the controller forward by dt
            controller.run(state, command)

            # Update the pwm widths going to the servos
            hardware_interface.set_actuator_postions(state.joint_angles)


run_robot_CreateLab()
