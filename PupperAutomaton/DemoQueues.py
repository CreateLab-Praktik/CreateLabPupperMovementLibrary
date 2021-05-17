from .BehaviorLibrary import *

def Test():
    """
        returns a queue that only activates and then deactivates the robot.
    """
    rawMessageQueue = list()

    rawMessageQueue.append(msg_Activation())
    rawMessageQueue.append(msg_Wait(20))
    rawMessageQueue.append(msg_Activation())
    rawMessageQueue.reverse()

    return rawMessageQueue

def ActiveMode():
    """
        returns a queue stacked with messages demoing activation, height, pitch, roll, and yaw messages.
    """

    rawMessageQueue = list()

    rawMessageQueue.append(msg_Activation())
    rawMessageQueue.append(msg_Wait(100))

    rawMessageQueue.append(msg_Height_Increase(20))
    rawMessageQueue.append(msg_Wait(20))

    rawMessageQueue.append(msg_Height_Decrease(20))
    rawMessageQueue.append(msg_Wait(20))

    rawMessageQueue.append(msg_Roll_Right(30))
    rawMessageQueue.append(msg_Wait(20))

    rawMessageQueue.append(msg_Roll_Left(30))
    rawMessageQueue.append(msg_Wait(20))

    rawMessageQueue.append(msg_Roll_Left(30))
    rawMessageQueue.append(msg_Wait(20))

    rawMessageQueue.append(msg_Roll_Right(30))
    rawMessageQueue.append(msg_Wait(20))

    rawMessageQueue.append(msg_Yaw_Left(20))
    rawMessageQueue.append(msg_Wait(30))

    rawMessageQueue.append(msg_Yaw_Right(40))
    rawMessageQueue.append(msg_Wait(20))

    rawMessageQueue.append(msg_Yaw_Left(20))
    rawMessageQueue.append(msg_Wait(30))

    rawMessageQueue.append(msg_Pitch_Up(20))
    rawMessageQueue.append(msg_Wait(20))

    rawMessageQueue.append(msg_Pitch_Down(40))
    rawMessageQueue.append(msg_Wait(20))

    rawMessageQueue.append(msg_Pitch_Up(20))
    rawMessageQueue.append(msg_Wait(20))
    

    ## reversing list since pop takes the last item.
    rawMessageQueue.reverse()

    return rawMessageQueue