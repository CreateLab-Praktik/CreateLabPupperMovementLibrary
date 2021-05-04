import numpy as np


class Command:
    """Stores movement command
    
    """

    def __init__(self, name = "none"):
        self.name = name
        self.horizontal_velocity = np.array([0, 0])
        self.yaw_rate = 0.0
        self.height = -0.16
        self.pitch = 0.0
        self.roll = 0.0
        self.activation = 0
        
        self.hop_event = False
        self.trot_event = False
        self.activate_event = False

    def toString(self) -> str:
        """ Returns the Commands name as a string
        """
        return self.name

    