import src.Command as Command
import CreateCommand as CreateCommand
from src.Controller import Controller
from src.State import State
from src.State import BehaviorState
from pupper.HardwareInterface import HardwareInterface
from pupper.Config import Configuration
from pupper.Kinematics import four_legs_inverse_kinematics
import queue

## load commands into list here
# TODO: Implement Command Inqueue Function
commandQueue = queue.SimpleQueue

numberOfCommands = len(commandQueue)

config = Configuration()
hardware_interface = HardwareInterface()

controller = Controller(
    config,
    four_legs_inverse_kinematics,
)

state = State()

while True:

    if numberOfCommands == 0:
        print("Error no commands loaded")
        break

    
    print("Switch to REST mode?")
    userInput = input("y/n: ")

    if userInput == "y":
        print("Robot Activated!")
        controller.run(state, CreateCommand.Activate_Command)
        hardware_interface.set_actuator_postions(state.joint_angles)

    elif userInput == "n":
        continue
    

    while numberOfCommands > 0:
        print("Execute this command? -> " + commandQueue[0].toString() )

        userInput = input("y/n: ")

        if userInput.lower == "y":
            

        
            
        



         

