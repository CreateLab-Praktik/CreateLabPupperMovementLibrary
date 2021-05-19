from .BehaviorLibrary import *
from .RawMessage import *
from .DemoQueues import test, behavioerDemo
import datetime

def transmissionLoopStart(TransmissionPipe, stopWhenEmpty = False):

    MESSAGE_RATE = 20

    pipe = TransmissionPipe
   
    rawMessageQueue = test()

    queueEmpty = False

    while True:

        if len(rawMessageQueue) <= 0:
            queueEmpty = True

        if len(rawMessageQueue) != 0:

            currentRawMsg = rawMessageQueue.pop()
            ticks = currentRawMsg.ticks
            messageDone = False

            while messageDone == False:

                pipe.send(currentRawMsg.parsed())
                stamp = datetime.datetime.now()
                print("Msg send", currentRawMsg.name, "At: ", stamp)
                ticks -= 1

                if ticks <= 0:
                    messageDone = True


        pipe.send(RawMessage().parsed())
        stamp = datetime.datetime
        print("Msg send", currentRawMsg.name, "At: ", stamp)

        if stopWhenEmpty == True and queueEmpty == True :
            break



