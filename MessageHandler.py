import UDPComms
import numpy as np
import time
from src.State import BehaviorState, State
from src.Command import Command
from src.Utilities import deadband, clipped_first_order_filter

class MessageHandler:
    """
        An object than can send and receive messages from a process pipe, and then turn those messages into commands. 
    """
    def __init__(self, config, TransmissionPipe):

        self.config = config
        self.previous_gait_toggle = 0
        self.previous_state = BehaviorState.REST
        self.previous_hop_toggle = 0
        self.previous_activate_toggle = 0

        self.message_rate = 50
        self.pipe = TransmissionPipe


    def get_command_from_pipe(self, state, do_print=False):
        
        msg = self.pipe.recv()
        command = Command()
        
        ####### Handle discrete commands ########
        # Check if requesting a state transition to trotting, or from trotting to resting
        gait_toggle = msg["trot"]
        command.trot_event = (gait_toggle == 1 and self.previous_gait_toggle == 0)

        # Check if requesting a state transition to hopping, from trotting or resting
        hop_toggle = msg["hop"]
        command.hop_event = (hop_toggle == 1 and self.previous_hop_toggle == 0)            
        
        activate_toggle = msg["activation"]
        command.activate_event = (activate_toggle == 1 and self.previous_activate_toggle == 0)

        # Update previous values for toggles and state
        self.previous_gait_toggle = gait_toggle
        self.previous_hop_toggle = hop_toggle
        self.previous_activate_toggle = activate_toggle

        ####### Handle continuous commands ########
        ## CreateLab Comment: It looks wierd that x_vel uses y_axis_velocity, i don't know why. 
        # I have checked if Stanfords does the same, and they do.  
        x_vel = msg["y_axis_velocity"] * self.config.max_x_velocity
        y_vel = msg["x_axis_velocity"] * -self.config.max_y_velocity
        command.horizontal_velocity = np.array([x_vel, y_vel])
        command.yaw_rate = msg["yaw"] * -self.config.max_yaw_rate

        message_rate = msg["message_rate"]
        print("Message Rate ------------------> ", message_rate)
        message_dt = 1.0 / message_rate
        print("Message downtime ------------------------>", message_dt)
        pitch = msg["pitch"] * self.config.max_pitch
        deadbanded_pitch = deadband(
            pitch, self.config.pitch_deadband
        )
        pitch_rate = clipped_first_order_filter(
            state.pitch,
            deadbanded_pitch,
            self.config.max_pitch_rate,
            self.config.pitch_time_constant,
        )
        command.pitch = state.pitch + message_dt * pitch_rate

        height_movement = msg["height"]
        command.height = state.height - message_dt * self.config.z_speed * height_movement
        
        roll_movement = - msg["roll"]
        command.roll = state.roll + message_dt * self.config.roll_speed * roll_movement

        return command



  