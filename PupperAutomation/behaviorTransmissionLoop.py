from .BehaviorLibrary import *
from .ActionMessage import *
from .DemoQueues import test, behavioerDemo, walkTest


def transmissionLoopStart(TransmissionPipe, stopWhenEmpty = False):

    pipe = TransmissionPipe
   
    actionMessageQueue = walkTest()

    queueEmpty = False

    while True:

        if len(actionMessageQueue) <= 0:
            queueEmpty = True

        if len(actionMessageQueue) != 0:

            currentActionMsg = actionMessageQueue.pop()
            ticks = currentActionMsg.ticks
            messageDone = False

            while messageDone == False:

                pipe.send(currentActionMsg.parsed())

                ticks -= 1

                if ticks <= 0:
                    messageDone = True


        pipe.send(ActionMessage().parsed())

        if stopWhenEmpty == True and queueEmpty == True :
            break



