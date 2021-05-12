#TODO move this class into its own space.
class RawMessage:
    def __init__(self, name = "Raw MSG"):
        """
            A message template that forms the basis for State altering commands.
                !must be parsed before robot can understand!

                name is used for debugging

                ticks are the duration or amount of ticks a message should be send   
        """
        self.ticks = 0
        self.name = name
        self.values = {
            "x_axis_velocity": 0,
            "y_axis_velocity": 0,
            "yaw": 0,
            "pitch": 0,
            "activation": 0,
            "trot": 0,
            "roll_right": 0,
            "roll_left": 0,
            "height_possitive": 0,
            "height_negative": 0,
            "hop": 0,
            }

def messageParser(RawMessage, MESSAGE_RATE = 20 ):
    """
        returnes a parsed message that can be parsed into a command by the Command Message Interface.
    """

    values = RawMessage.values

    yaw = values["yaw"]
    pitch = -values["pitch"]
    x_axis_velocity = values["x_axis_velocity"]
    y_axis_velocity = -values["y_axis_velocity"]

    activation = values["activation"]
    trot = values["trot"]
    hop = values["hop"]

    roll = values["roll_right"] - values["roll_left"]
    height = values["height_possitive"] - values["height_negative"]

    parsedMessage = {

        "yaw": yaw,
        "pitch": pitch,
        "y_axis_velocity": y_axis_velocity,
        "x_axis_velocity": x_axis_velocity,
        
        "activation": activation,
        "trot": trot,
        "roll": roll,

        "height": height,
        "hop": hop,
        "message_rate": MESSAGE_RATE,
    }

    return parsedMessage

########################################## Behavior functions below here ############################################

############### Utility functions

def raw_msg_Wait(ticks = 20):
    rawMessage = RawMessage("Waiting")
    rawMessage.ticks = ticks

    return rawMessage

############### Mode switching functions

def raw_msg_Activation():

    rawMessage = RawMessage("Activation")
    rawMessage.values["activation"] = 1

    return rawMessage

def raw_msg_Trot():

    rawMessage = RawMessage("Trot")
    rawMessage.values["trot"] = 1
 
    return rawMessage

############## Heigth and Roll functions

def raw_msg_Height_Increase(ticks = 0):

    rawMessage = RawMessage("Increasing Height")
    rawMessage.values["height_possitive"] = 1
    rawMessage.ticks = ticks
  
    return rawMessage

    
def raw_msg_Height_Decrease(ticks = 0):

    rawMessage = RawMessage("Decreasing Height")
    rawMessage.values["height_negative"] = 1
    rawMessage.ticks = ticks
  
    return rawMessage

def raw_msg_Roll_Right(ticks = 0):

    rawMessage = RawMessage("Roll MSG")
    rawMessage.values["roll_right"] = 1
    rawMessage.ticks = ticks

    return rawMessage

    
def raw_msg_Roll_Left(ticks = 0, right = True):

    rawMessage = RawMessage("Roll MSG")
    rawMessage.values["roll_left"] = 1
    rawMessage.ticks = ticks

    return rawMessage   

############## Yaw and Pitch functions

def raw_msg_Yaw_Left(ticks = 0):
    rawMessage = RawMessage("Yaw left")
    rawMessage.values["yaw"] = -1
    rawMessage.ticks = ticks

    return rawMessage

def raw_msg_Yaw_Right(ticks = 0):
    rawMessage = RawMessage("Yaw Right")
    rawMessage.values["yaw"] = 1
    rawMessage.ticks = ticks

    return rawMessage

def raw_msg_Pitch_Up(ticks = 0):
    rawMessage = RawMessage("Pitch Up")
    rawMessage.values["pitch"] = -1
    rawMessage.ticks = ticks

    return rawMessage

def raw_msg_Pitch_Down(ticks = 0):
    rawMessage = RawMessage("Pitch Down")
    rawMessage.values["pitch"] = 1
    rawMessage.ticks = ticks

    return rawMessage