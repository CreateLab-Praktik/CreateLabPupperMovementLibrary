from .ActionMessage import ActionMessage

############### Utility functions

def msg_Wait(ticks = 20):
    actionMessage = ActionMessage("Waiting")
    actionMessage.ticks = ticks
    
    return actionMessage

############### Mode switching functions


def msg_Activation():

    actionMessage = ActionMessage("Activation")
    actionMessage.activation = 1

    return actionMessage

def msg_Trot(interrupt: bool = False):

    actionMessage = ActionMessage("Trot")
    actionMessage.trot = 1
    actionMessage.interrupt = interrupt
 
    return actionMessage

############## Heigth and Roll functions

def msg_Height_Increase(ticks = 0):

    actionMessage = ActionMessage("Increasing Height")
    actionMessage.height_possitive = 1
    actionMessage.ticks = ticks
  
    return actionMessage

    
def msg_Height_Decrease(ticks = 0):

    actionMessage = ActionMessage("Decreasing Height")
    actionMessage.height_negative = 1
    actionMessage.ticks = ticks
  
    return actionMessage

def msg_Roll_Right(ticks = 0):

    actionMessage = ActionMessage("Roll MSG")
    actionMessage.roll_right = 1
    actionMessage.ticks = ticks

    return actionMessage

    
def msg_Roll_Left(ticks = 0, right = True):

    actionMessage = ActionMessage("Roll MSG")
    actionMessage.roll_left = 1
    actionMessage.ticks = ticks

    return actionMessage

############## Yaw and Pitch functions

def msg_Yaw_Right(ticks = 0):
    actionMessage = ActionMessage("Yaw right")
    actionMessage.yaw = 1
    actionMessage.ticks = ticks

    return actionMessage

def msg_Yaw_Left(ticks = 0):
    actionMessage = ActionMessage("Yaw left")
    actionMessage.yaw = -1
    actionMessage.ticks = ticks

    return actionMessage

def msg_Pitch_Up(ticks = 0):
    actionMessage = ActionMessage("Pitch Up")
    actionMessage.pitch = -1
    actionMessage.ticks = ticks

    return actionMessage

def msg_Pitch_Down(ticks = 0):
    actionMessage = ActionMessage("Pitch Down")
    actionMessage.pitch = 1
    actionMessage.ticks = ticks

    return actionMessage

############## Forwards, Backwards, Strafing(right and left), momentum functions.

def msg_Forwards(ticks = 0):
    actionMessage = ActionMessage("forwards")
    actionMessage.y_axis_velocity = -1
    actionMessage.ticks = ticks

    return actionMessage

def msg_Backwards(ticks = 0):
    actionMessage = ActionMessage("backwards")
    actionMessage.y_axis_velocity = 1
    actionMessage.ticks = ticks

    return actionMessage

def msg_Strafe_Right(ticks = 0):
    actionMessage = ActionMessage("strafe right")
    actionMessage.x_axis_velocity = 1
    actionMessage.ticks = ticks

    return actionMessage

def msg_Strafe_Left(ticks = 0):
    actionMessage = ActionMessage("strafe left")
    actionMessage.x_axis_velocity = -1
    actionMessage.ticks = ticks

    return actionMessage

############## Right and Left turning functions

def msg_Turn_Right(ticks = 0):
    actionMessage = ActionMessage("turn right")
    actionMessage.y_axis_velocity = -1
    actionMessage.yaw = 1
    actionMessage.ticks = ticks

    return actionMessage

def msg_Turn_Left(ticks = 0):
    actionMessage = ActionMessage("turn left")
    actionMessage.y_axis_velocity = -1
    actionMessage.yaw = -1
    actionMessage.ticks = ticks

    return actionMessage