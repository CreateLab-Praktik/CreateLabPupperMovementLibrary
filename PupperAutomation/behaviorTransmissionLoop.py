from .BehaviorLibrary import *
from .RawMessage import *
from .DemoQueues import test, behavioerDemo
import time


def transmissionLoopStart(TransmissionPipe, stopWhenEmpty = False):

    ## Configurable ##
    MESSAGE_RATE = 20

    pipe = TransmissionPipe
   
    rawMessageQueue = behavioerDemo()

        ## Raw message Loop

    while True:
        print("Message loop started")
        print("message count: ", len(rawMessageQueue))

        queueEmpty = False

        if len(rawMessageQueue) <= 0:
            queueEmpty = True

        if len(rawMessageQueue) != 0:
            currentRawMsg = rawMessageQueue.pop()
            ticks = currentRawMsg.ticks
            flag = 1
            while flag == 1:
                pipe.send(currentRawMsg.parsed())
                print("Msg send", currentRawMsg.name)
                #TODO Figure out why sleep is required.
                time.sleep(1 / MESSAGE_RATE)
                ticks -= 1
                if ticks <= 0:
                    flag = 0


        pipe.send(RawMessage().parsed())
        print("Raw MSG send")

        if stopWhenEmpty == True and queueEmpty == True :
            break



