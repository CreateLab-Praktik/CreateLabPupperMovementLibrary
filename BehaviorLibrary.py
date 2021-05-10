
class RawMessage:
    def __init__(self, name = "Raw MSG"):

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

        self.duration = 0

        self.name = name
        


def raw_Activation_Msg():
    rawMessage = RawMessage()

    rawMessage.values["activation"] = 1
    rawMessage.name = "Activation MSG"

    return rawMessage

def raw_Trot_Msg():
    rawMessage = RawMessage()

    rawMessage.values["trot"] = 1

    return rawMessage

def raw_Height_Msg(amount = 0):
    ## TODO catch illigal amounts.
    """
        returns a message where the height value is equal to amount.

        amount MUST NEVER be greater than 1 or lower than -1.    
    """
    rawMessage = RawMessage()

    rawMessage.values["height"] = 1
    rawMessage.duration = amount
    rawMessage.name = "Height MSG"

    return rawMessage


def messageParser(RawMessage, MESSAGE_RATE = 20 ):

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