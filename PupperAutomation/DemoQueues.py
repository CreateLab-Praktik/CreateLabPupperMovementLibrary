from .BehaviorLibrary import *

def walkTest():
    actionsMessageQueue = list()

    actionsMessageQueue.append(msg_Activation())
    actionsMessageQueue.append(msg_Wait(200))
    actionsMessageQueue.append(msg_Trot())
    actionsMessageQueue.append(msg_Forwards(200))
    actionsMessageQueue.append(msg_Wait(50))
    actionsMessageQueue.append(msg_Strafe_Right(200))
    actionsMessageQueue.append(msg_Wait(50))
    actionsMessageQueue.append(msg_Strafe_Left(200))
    actionsMessageQueue.append(msg_Wait(50))
    actionsMessageQueue.append(msg_Backwards(200))
    actionsMessageQueue.append(msg_Wait(200))
    actionsMessageQueue.append(msg_Trot())
    actionsMessageQueue.reverse()

    return actionsMessageQueue

def test():
    """
        returns a queue that only activates and then deactivates the robot.
    """
    actionsMessageQueue = list()

    actionsMessageQueue.append(msg_Activation())
    actionsMessageQueue.append(msg_Wait(20))
    actionsMessageQueue.append(msg_Trot())
    actionsMessageQueue.append(msg_Wait(2000))
    actionsMessageQueue.append(msg_Trot())
    actionsMessageQueue.reverse()

    return actionsMessageQueue

def behavioerDemo():
    """
        returns a queue stacked with messages demoing activation, height, pitch, roll, and yaw messages.
    """

    actionsMessageQueue = list()

    actionsMessageQueue.append(msg_Activation())
    actionsMessageQueue.append(msg_Wait(100))

    actionsMessageQueue.append(msg_Height_Increase(60))
    actionsMessageQueue.append(msg_Wait(20))

    actionsMessageQueue.append(msg_Height_Decrease(60))
    actionsMessageQueue.append(msg_Wait(20))

    actionsMessageQueue.append(msg_Roll_Right(30))
    actionsMessageQueue.append(msg_Wait(20))

    actionsMessageQueue.append(msg_Roll_Left(30))
    actionsMessageQueue.append(msg_Wait(20))

    actionsMessageQueue.append(msg_Roll_Left(30))
    actionsMessageQueue.append(msg_Wait(20))

    actionsMessageQueue.append(msg_Roll_Right(30))
    actionsMessageQueue.append(msg_Wait(20))

    actionsMessageQueue.append(msg_Yaw_Left(20))
    actionsMessageQueue.append(msg_Wait(30))

    actionsMessageQueue.append(msg_Yaw_Right(40))
    actionsMessageQueue.append(msg_Wait(20))

    actionsMessageQueue.append(msg_Yaw_Left(20))
    actionsMessageQueue.append(msg_Wait(30))

    actionsMessageQueue.append(msg_Pitch_Up(20))
    actionsMessageQueue.append(msg_Wait(20))

    actionsMessageQueue.append(msg_Pitch_Down(40))
    actionsMessageQueue.append(msg_Wait(20))

    actionsMessageQueue.append(msg_Pitch_Up(20))
    actionsMessageQueue.append(msg_Wait(20))
    

    ## reversing list since pop takes the last item.
    actionsMessageQueue.reverse()

    return actionsMessageQueue