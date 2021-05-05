import behaviorOutput as behaviorOutput

from UDPComms import Publisher, Subscriber, timeout


import time

## Configurable ##
MESSAGE_RATE = 20

publisher = Publisher(8830)
subcriber = Subscriber(8840, timeout=0.01)


while True:
    print("running")
    values = get_input()

    right_x = values["right_analog_x"]
    right_y = -values["right_analog_y"]
    left_x = values["left_analog_x"]
    left_y = -values["left_analog_y"]

    activation = values["activation"]
    trot = values["trot"]
    hop = values["hop"]

    roll = values["roll_right"] - values["roll_left"]
    height = values["height_possitive"] - values["height_negative"]

    msg = {
        "ly": left_y,
        "lx": left_x,
        "rx": right_x,
        "ry": right_y,
        "activation": activation,
        "trot": trot,
        "roll": roll,
        "height": height,
        "hop": hop,
        "message_rate": MESSAGE_RATE,
    }
    
    publisher.send(msg)

    try:
        msg = subcriber.get()
    except timeout:
        pass

    time.sleep(1 / MESSAGE_RATE)
