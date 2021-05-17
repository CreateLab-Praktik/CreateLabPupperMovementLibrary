import CreateLabPupper.RawMessage as RawMsg


############### Utility functions

def msg_Wait(ticks = 20):
    rawMessage = RawMsg.RawMessage("Waiting")
    rawMessage.ticks = ticks

    return rawMessage

############### Mode switching functions


def msg_Activation():

    rawMessage = RawMsg.RawMessage("Activation")
    rawMessage.values["activation"] = 1

    return rawMessage

def msg_Trot():

    rawMessage = RawMsg.RawMessage("Trot")
    rawMessage.values["trot"] = 1
 
    return rawMessage

############## Heigth and Roll functions

def msg_Height_Increase(ticks = 0):

    rawMessage = RawMsg.RawMessage("Increasing Height")
    rawMessage.values["height_possitive"] = 1
    rawMessage.ticks = ticks
  
    return rawMessage

    
def msg_Height_Decrease(ticks = 0):

    rawMessage = RawMsg.RawMessage("Decreasing Height")
    rawMessage.values["height_negative"] = 1
    rawMessage.ticks = ticks
  
    return rawMessage

def msg_Roll_Right(ticks = 0):

    rawMessage = RawMsg.RawMessage("Roll MSG")
    rawMessage.values["roll_right"] = 1
    rawMessage.ticks = ticks

    return rawMessage

    
def msg_Roll_Left(ticks = 0, right = True):

    rawMessage = RawMsg.RawMessage("Roll MSG")
    rawMessage.values["roll_left"] = 1
    rawMessage.ticks = ticks

    return rawMessage

############## Yaw and Pitch functions

def msg_Yaw_Left(ticks = 0):
    rawMessage = RawMsg.RawMessage("Yaw left")
    rawMessage.values["yaw"] = -1
    rawMessage.ticks = ticks

    return rawMessage

def msg_Yaw_Right(ticks = 0):
    rawMessage = RawMsg.RawMessage("Yaw Right")
    rawMessage.values["yaw"] = 1
    rawMessage.ticks = ticks

    return rawMessage

def msg_Pitch_Up(ticks = 0):
    rawMessage = RawMsg.RawMessage("Pitch Up")
    rawMessage.values["pitch"] = -1
    rawMessage.ticks = ticks

    return rawMessage

def msg_Pitch_Down(ticks = 0):
    rawMessage = RawMsg.RawMessage("Pitch Down")
    rawMessage.values["pitch"] = 1
    rawMessage.ticks = ticks

    return rawMessage