import BehaviorLibrary as BL

def TrotMode():
    rawMessageQueue = list()

    rawMessageQueue.append(BL.raw_msg_Activation())
    rawMessageQueue.append(BL.raw_msg_Wait(50))

    rawMessageQueue.append(BL.raw_msg_Trot())

   
    rawMessageQueue.reverse()

    return rawMessageQueue
def ActiveMode():
    """
        Return a queue stacked with messages demoing an activation, including height, pitch, roll, and yaw.
    """

    rawMessageQueue = list()

    rawMessageQueue.append(BL.raw_msg_Activation())
    rawMessageQueue.append(BL.raw_msg_Wait(100))

    rawMessageQueue.append(BL.raw_msg_Height_Increase(20))
    rawMessageQueue.append(BL.raw_msg_Wait(20))

    rawMessageQueue.append(BL.raw_msg_Height_Decrease(20))
    rawMessageQueue.append(BL.raw_msg_Wait(20))

    rawMessageQueue.append(BL.raw_msg_Roll_Right(30))
    rawMessageQueue.append(BL.raw_msg_Wait(20))

    rawMessageQueue.append(BL.raw_msg_Roll_Left(30))
    rawMessageQueue.append(BL.raw_msg_Wait(20))

    rawMessageQueue.append(BL.raw_msg_Roll_Left(30))
    rawMessageQueue.append(BL.raw_msg_Wait(20))

    rawMessageQueue.append(BL.raw_msg_Roll_Right(30))
    rawMessageQueue.append(BL.raw_msg_Wait(20))

    rawMessageQueue.append(BL.raw_msg_Yaw_Left(20))
    rawMessageQueue.append(BL.raw_msg_Wait(30))

    rawMessageQueue.append(BL.raw_msg_Yaw_Right(40))
    rawMessageQueue.append(BL.raw_msg_Wait(20))

    rawMessageQueue.append(BL.raw_msg_Yaw_Left(20))
    rawMessageQueue.append(BL.raw_msg_Wait(30))

    rawMessageQueue.append(BL.raw_msg_Pitch_Up(20))
    rawMessageQueue.append(BL.raw_msg_Wait(20))

    rawMessageQueue.append(BL.raw_msg_Pitch_Down(40))
    rawMessageQueue.append(BL.raw_msg_Wait(20))

    rawMessageQueue.append(BL.raw_msg_Pitch_Up(20))
    rawMessageQueue.append(BL.raw_msg_Wait(20))
    

    ## reversing list since pop takes the last item.
    rawMessageQueue.reverse()

    return rawMessageQueue