import BehaviorLibrary as BL
import RawMessage as RawMsg
import DemoQueues as Demos
import time


def start(TransmissionPipe, stopWhenEmpty = False):

    ## Configurable ##
    MESSAGE_RATE = 20

    pipe = TransmissionPipe
   
    rawMessageQueue = Demos.TrotMode()

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
                time.sleep(1 / MESSAGE_RATE)
                ticks -= 1
                if ticks <= 0:
                    flag = 0

        

            
        pipe.send(RawMsg.RawMessage().parsed())
        print("Raw MSG send")

        if stopWhenEmpty == True and queueEmpty == True :
            break

        time.sleep(1 / MESSAGE_RATE)



