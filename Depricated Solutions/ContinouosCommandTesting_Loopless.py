import CreateCommand as CreateCommand
from src.Controller import Controller
from src.State import State
from src.State import BehaviorState
from pupper.HardwareInterface import HardwareInterface
from pupper.Config import Configuration
from pupper.Kinematics import four_legs_inverse_kinematics
import queue
import time


config = Configuration()
hardware_interface = HardwareInterface()

controller = Controller(
    config,
    four_legs_inverse_kinematics,
)

state = State()

print("Activating Robot")
command_01 = CreateCommand.command_Activate()

time.sleep(1.0)
controller.run(state, command_01)
time.sleep(0.1)
hardware_interface.set_actuator_postions(state.joint_angles)
time.sleep(1.0)

state.printBehaviorState()

print("Robot activated")

input("Continue...?")

print("Sending TROT Event")
command_02 = CreateCommand.command_Trot_Event()

time.sleep(1.0)
controller.run(state, command_02)
time.sleep(0.1)
hardware_interface.set_actuator_postions(state.joint_angles)

time.sleep(1.0)

state.printBehaviorState()

time.sleep(5.0)

print("Sending TROT Event")
command_02 = CreateCommand.command_Trot_Event()

time.sleep(1.0)
controller.run(state, command_02)
time.sleep(0.1)
hardware_interface.set_actuator_postions(state.joint_angles)

state.printBehaviorState()
            

        
            
        



         

