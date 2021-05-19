from .BehaviorLibrary import *
from .RawMessage import *
from .DemoQueues import test, behavioerDemo


def transmissionLoopStart(TransmissionPipe, stopWhenEmpty = False):

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

                ticks -= 1

                if ticks <= 0:
                    messageDone = True


        pipe.send(RawMessage().parsed())

        if stopWhenEmpty == True and queueEmpty == True :
            break



