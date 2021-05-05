
def newRawMessage():
    message = {
        "x_axis_velocity": 512,
        "y_axis_velocity": 512,
        "yaw": 512,
        "pitch": 512,
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

# def walkForwards(3):

# def stop(wait 2 seconds):

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

        "rx": yaw,
        "ry": pitch,
        "ly": y_axis_velocity,
        "lx": x_axis_velocity,
        
        "activation": activation,
        "trot": trot,
        "roll": roll,

        "height": height,
        "hop": hop,
        "message_rate": MESSAGE_RATE,
    }

    return parsedMessage