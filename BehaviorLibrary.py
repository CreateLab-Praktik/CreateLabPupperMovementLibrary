
def newRawMessage():
    message = {
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

    return message

def message_Activation():
    message = newRawMessage()

    message["activation"] = 1

    return message

def message_Trot():
    message = newRawMessage()

    message["trot"] = 1

    return message

def message_height(amount = 0):
    ## TODO catch illigal amounts.
    """
        returns a message where the height value is equal to amount.

        amount MUST NEVER be greater than 1 or lower than -1.    
    """
    message = newRawMessage()

    message["height"] = amount

    return message


def messageParser(RawMessage = newRawMessage(), MESSAGE_RATE = 20 ):

    values = RawMessage

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